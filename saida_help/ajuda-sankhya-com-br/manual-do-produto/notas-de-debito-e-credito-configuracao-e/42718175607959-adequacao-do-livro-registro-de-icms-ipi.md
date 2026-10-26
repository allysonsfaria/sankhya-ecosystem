---
id: "42718175607959"
titulo: "Adequação do Livro Registro de ICMS/IPI às Notas de Débito e Crédito – Ajuste SINIEF 49/2025"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42718175607959-Adequa%C3%A7%C3%A3o-do-Livro-Registro-de-ICMS-IPI-%C3%A0s-Notas-de-D%C3%A9bito-e-Cr%C3%A9dito-Ajuste-SINIEF-49-2025"
trilha: "Manual do Produto > Fiscal e Contábil > Reforma Tributária > Notas de Débito e Crédito - Configuração e Emissão"
atualizado_em: "2026-08-14T12:09:22Z"
---

# Adequação do Livro Registro de ICMS/IPI às Notas de Débito e Crédito – Ajuste SINIEF 49/2025

Com o Ajuste SINIEF 49/2025, apenas determinados tipos de Notas de Débito (finNFe = 6) e Notas de Crédito (finNFe = 5) devem ser escriturados no Livro ICMS/IPI, conforme as restrições previstas no Guia Prático da EFD ICMS/IPI v3.2.2.

O Sankhya foi aprimorado para garantir a conformidade com o novo modelo documental, bloqueando a escrituração de documentos que não atendem aos critérios de elegibilidade.

Tipos de documentos permitidos na escrituração do Livro ICMS/IPI:

Notas de Débito:

- Tipo 06 — Venda para Entrega Futura com Pagamento Antecipado
- Tipo 07 — Baixa de Estoque (Perda, Roubo ou Deterioração)

Notas de Crédito:

- Tipo 03 — Retorno de Mercadoria (Recusa ou Não Localização)
- Tipo 04 — Redução de Valores ou Quantidades

| Atenção:  Demais tipos de Notas de Débito e Crédito não serão registrados no Livro ICMS/IPI. Esses documentos não impactarão os totalizadores do livro e não afetarão as bases e valores demonstrativos. |
| --- |

O sistema aplica as mesmas regras de validação do Livro ICMS/IPI durante o processo de geração, garantindo a integridade e conformidade dos dados fiscais.

**Tratamento de Estornos de Crédito de ICMS:**

Os estornos de crédito decorrentes das operações previstas no Ajuste SINIEF 49/2025 são atendidos através da rotina existente de "Configuração de Ajustes Fiscais". A parametrização permite:

- Geração de Registro C197 quando houver código específico por UF
- Utilização do Registro E111 para ajustes de apuração consolidados
- Definição de códigos estaduais conforme legislação aplicável

Exemplos de configuração por UF:

- Minas Gerais: Observar Tabela 5.1.1 da EFD ICMS/IPI e Portaria SAIF 001/2009 (priorizar ajuste por documento - C197)
- Ceará: Utilizar código padrão CE010016
