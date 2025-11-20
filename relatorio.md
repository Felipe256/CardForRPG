# Relatório CFA

1. Introdução

Este documento detalha a **codificação completa da ficha de personagem do RPG *Ordem Paranormal*** em cartões **MIFARE Classic 1K**, com integração via **ESP32-C3 + PN532** e controle remoto pelo **aplicativo do mestre via Wi-Fi**.

A estrutura é dividida em **3 fases de implementação**, permitindo entregas incrementais funcionais. Todos os dados são armazenados como **strings UTF-8**, separados por `;` e preenchidos com `\x00` até 16 bytes por bloco.

> **Capacidade do cartão:** 768 bytes úteis (48 blocos de 16 bytes).

> **Uso total estimado:** **659 bytes** (41 blocos) → **cabe com folga**

---

## 2. Estrutura Geral do Cartão

| **Característica** | **Valor**                     |
| ------------------ | ----------------------------- |
| Modelo             | MIFARE Classic 1K             |
| Capacidade total   | 1024 bytes                    |
| Blocos de dados    | 48 (768 bytes úteis)          |
| Blocos de trailer  | 16 (reservados para chaves)   |
| Autenticação       | Chave A padrão (`0xFF...FF`)  |
| Codificação        | UTF-8                         |
| Separador          | `;`                           |
| Preenchimento      | `\x00` até 16 bytes por bloco |
| Formato de vetor   | `[12,34,56]`                  |
| Tabela de consulta | No app do mestre              |

---

## 3. Fases do Projeto

### Fase 1: Dados Básicos da Ficha

**Objetivo:** Ler/escrever dados essenciais via Wi-Fi.

#### Campos (com tamanho máximo):

| **Sigla** | **Nome**        | **Tamanho**   | **Exemplo**        |
| --------- | --------------- | ------------- | ------------------ |
| NOM       | Nome            | 20 chars      | `João Silva`       |
| ORI       | Origem          | 2 dígitos     | `10`               |
| CLA       | Classe          | 2 dígitos     | `11`               |
| PV        | Vida Atual      | 3 dígitos     | `012`              |
| PVM       | Vida Máxima     | 3 dígitos     | `015`              |
| SAN       | Sanidade Atual  | 3 dígitos     | `050`              |
| SNM       | Sanidade Máxima | 3 dígitos     | `060`              |
| PE        | Esforço Atual   | 3 dígitos     | `010`              |
| PEM       | Esforço Máximo  | 3 dígitos     | `012`              |
| CND       | Condições       | 5 × 2 dígitos | `[12,34,56,78,90]` |
| DEF       | Defesa          | 2 dígitos     | `08`               |
| ESQ       | Esquiva         | 2 dígitos     | `10`               |
| BLQ       | Bloqueio        | 2 dígitos     | `05`               |
| CAR       | Carga Atual     | 2 dígitos     | `08`               |
| CRM       | Carga Máxima    | 2 dígitos     | `15`               |

**Blocos usados:** 4 e 5

**Tamanho total:** 143 bytes (9 blocos)

---

### Fase 2: Perícias e Atributos

**Objetivo:** Cálculo automático de perícias com base em atributos.

#### Atributos (5):

| **Sigla** | **Nome**  | **Tamanho** |
| --------- | --------- | ----------- |
| FOR       | Força     | 1 dígito    |
| AGI       | Agilidade | 1 dígito    |
| INT       | Intelecto | 1 dígito    |
| VIG       | Vigor     | 1 dígito    |
| PRE       | Presença  | 1 dígito    |

#### Perícias (28):

| **Sigla** | **Nome**     | **Tamanho** |
| --------- | ------------ | ----------- |
| ACR       | Acrobacia    | 2 dígitos   |
| ADE       | Adestramento | 2 dígitos   |
| ART       | Artes        | 2 dígitos   |
| ATL       | Atletismo    | 2 dígitos   |
| COM       | Combate      | 2 dígitos   |
| CON       | Conhecimento | 2 dígitos   |
| CUL       | Cultura      | 2 dígitos   |
| DIS       | Discrição    | 2 dígitos   |
| ENG       | Engenharia   | 2 dígitos   |
| FIG       | Fuga         | 2 dígitos   |
| FRA       | Fraqueza     | 2 dígitos   |
| INV       | Investigação | 2 dígitos   |
| OCU       | Ocultismo    | 2 dígitos   |
| INT       | Intuição     | 2 dígitos   |
| JOG       | Jogo         | 2 dígitos   |
| LAB       | Laboratório  | 2 dígitos   |
| MED       | Medicina     | 2 dígitos   |
| NAT       | Natureza     | 2 dígitos   |
| NAV       | Navegação    | 2 dígitos   |
| PER       | Percepção    | 2 dígitos   |
| PIL       | Pilotagem    | 2 dígitos   |
| PSI       | Psicologia   | 2 dígitos   |
| REF       | Reflexos     | 2 dígitos   |
| REL       | Religião     | 2 dígitos   |
| SEG       | Segurança    | 2 dígitos   |
| SOC       | Social       | 2 dígitos   |
| TEC       | Tecnologia   | 2 dígitos   |

**Blocos usados:** 6, 8–16

**Tamanho total:** 226 bytes (14 blocos)

---

### Fase 3: Rituais, Poderes e Itens

**Objetivo:** Aplicar efeitos automáticos de itens, condições e rituais.

#### Campos:

| **Sigla** | **Nome**            | **Tamanho**    |
| --------- | ------------------- | -------------- |
| RIT       | Rituais             | 30 × 3 dígitos |
| POD       | Poderes Paranormais | 8 × 3 dígitos  |
| ITM       | Itens               | 30 × 3 dígitos |

**Blocos usados:** 20–35

**Tamanho total:** 290 bytes (18 blocos)

---

## 4. Mapeamento de Blocos

| **Bloco** | **Conteúdo**                                   |
| --------- | ---------------------------------------------- |
| 4         | NOM, ORI, CLA, PV, PVM, SAN, SNM, PE, PEM, CND |
| 5         | DEF, ESQ, BLQ, CAR, CRM                        |
| 6         | FOR, AGI, INT, VIG, PRE                        |
| 8–14      | Perícias (4 por bloco)                         |
| 15–16     | Reservado (perícias extras)                    |
| 20–26     | RIT (vetor 30 × 3)                             |
| 27–28     | POD (vetor 8 × 3)                              |
| 29–35     | ITM (vetor 30 × 3)                             |

---

## 5. Cálculo de Espaço (1 caractere = 1 byte)

| **Campo**        | **Cálculo**                                     | **Bytes** |
| ---------------- | ----------------------------------------------- | --------- |
| NOM              | `NOM:` (4) + 20 + `;` = 25                      | **25**    |
| ORI              | `ORI:` (4) + 2 + `;` = 7                        | **7**     |
| CLA              | `CLA:` (4) + 2 + `;` = 7                        | **7**     |
| PV               | `PV:` (3) + 3 + `;` = 7                         | **7**     |
| PVM              | `PVM:` (4) + 3 + `;` = 8                        | **8**     |
| SAN              | `SAN:` (4) + 3 + `;` = 8                        | **8**     |
| SNM              | `SNM:` (4) + 3 + `;` = 8                        | **8**     |
| PE               | `PE:` (3) + 3 + `;` = 7                         | **7**     |
| PEM              | `PEM:` (4) + 3 + `;` = 8                        | **8**     |
| CND              | `CND:` (4) + `[12,34,56,78,90]` (15) + `;` = 20 | **20**    |
| DEF              | `DEF:` (4) + 2 + `;` = 7                        | **7**     |
| ESQ              | `ESQ:` (4) + 2 + `;` = 7                        | **7**     |
| BLQ              | `BLQ:` (4) + 2 + `;` = 7                        | **7**     |
| CAR              | `CAR:` (4) + 2 + `;` = 7                        | **7**     |
| CRM              | `CRM:` (4) + 2 + `;` = 7                        | **7**     |
| **Fase 1 Total** |                                                 | **143**   |

| Atributos (5) | 5 × (4 + 1 + 1) = 30 | **30** | | Perícias (28) | 28 × (4 + 2 + 1) = 196 | **196** | | **Fase 2 Total** | | **226** |

| RIT | `RIT:` (4) + `[123,...,999]` (126) + `;` = 131 | **131** | | POD | `POD:` (4) + `[123,...,999]` (38) + `;` = 43 | **43** | | ITM | `ITM:` (4) + `[123,...,999]` (126) + `;` = 131 | **131** | | **Fase 3 Total** | | **305** |

> **Total Geral:** 143 + 226 + 305 = **674 bytes**

> **Blocos necessários:** 42 de 48

> **Sobra:** 94 bytes (6 blocos)