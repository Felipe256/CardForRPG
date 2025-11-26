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
| NEX       | NEX             | 2 dígitos     | `05`               |
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

| **Sigla** | **Nome**       | **Tamanho** |
| --------- | -------------- | ----------- |
| ACR       | Acrobacia      | 1 dígito    |
| ADE       | Adestramento   | 1 dígito    |
| ART       | Artes          | 1 dígito    |
| ATL       | Atletismo      | 1 dígito    |
| ATU       | Atualidades    | 1 dígito    |
| CIE       | Ciências       | 1 dígito    |
| CRI       | Crime          | 1 dígito    |
| DIP       | Diplomacia     | 1 dígito    |
| ENG       | Enganação      | 1 dígito    |
| FOR       | Fortitude      | 1 dígito    |
| FUR       | Furtividade    | 1 dígito    |
| INI       | Iniciativa     | 1 dígito    |
| ITM       | Intimidação    | 1 dígito    |
| ITU       | Intuição       | 1 dígito    |
| INV       | Investigação   | 1 dígito    |
| LUT       | Luta           | 1 dígito    |
| MED       | Medicina       | 1 dígito    |
| OCU       | Ocultismo      | 1 dígito    |
| PER       | Percepção      | 1 dígito    |
| PIL       | Pilotagem      | 1 dígito    |
| PON       | Pontaria       | 1 dígito    |
| PRO       | Profissão      | 1 dígito    |
| REF       | Reflexos       | 1 dígito    |
| REL       | Religião       | 1 dígito    |
| SOB       | Sobrevivência  | 1 dígito    |
| TAT       | Tática         | 1 dígito    |
| TEC       | Tecnologia     | 1 dígito    |
| VON       | Vontade        | 1 dígito    |

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

| **Bloco** | **Conteúdo**                                        |
| --------- | --------------------------------------------------- |
| 4         | NOM, ORI, CLA, NEX, PV, PVM, SAN, SNM, PE, PEM, CND |
| 5         | DEF, ESQ, BLQ, CAR, CRM                             |
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
| NEX              | `NEX:` (4) + 2 + `;` = 7                        | **7**     |
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
| **Fase 1 Total** |                                                 | **150**   |

| Atributos (5) | 5 × (4 + 1 + 1) = 30 | **30** | | Perícias (28) | 28 × (4 + 1 + 1) = 168 | **168** | | **Fase 2 Total** | | **198** |

| RIT | `RIT:` (4) + `[123,...,999]` (126) + `;` = 131 | **131** | | POD | `POD:` (4) + `[123,...,999]` (38) + `;` = 43 | **43** | | ITM | `ITM:` (4) + `[123,...,999]` (126) + `;` = 131 | **131** | | **Fase 3 Total** | | **305** |

> **Total Geral:** 150 + 198 + 305 = **653 bytes**

> **Blocos necessários:** 41 de 48

> **Sobra:** 115 bytes (7 blocos)