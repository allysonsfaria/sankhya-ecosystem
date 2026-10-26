---
id: "360044513733"
titulo: "Crédito Extemporâneo - Registro G126 do SPED FISCAL"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044513733-Cr%C3%A9dito-Extempor%C3%A2neo-Registro-G126-do-SPED-FISCAL"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:56:13Z"
rotulos: ["#RevisadoJR", "Configuração", "Fiscal", "Crédito", "ICMS", "Impostos", "EFD", "Créditos ICMS não escriturados", "Parâmetros CIAP corretos", "Configuração Bloco G126"]
---

# Crédito Extemporâneo - Registro G126 do SPED FISCAL

![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17800089571607) **SITUAÇÃO:**

Este registro tem por objetivo discriminar os demais valores a serem apropriados como créditos de ICMS de Ativo Imobilizado que não foram escriturados nos períodos anteriores, quando a legislação permitir.

**(1)** **Regras para geração do Registro G126:**

![Imagem 2: Na tela 'Empresa' (Comercial » Preferências » Empresa) - Aba EFD- Escrituração Fiscal Digital » Tipo de Escrituração =…](https://ajuda.sankhya.com.br/hc/article_attachments/17800067606935) Na tela 'Empresa' (Comercial » Preferências » Empresa) - Aba EFD- Escrituração Fiscal Digital » Tipo de Escrituração = EFD, certificar-se que o Registro/Bloco abaixo foi configurado:

- Bloco G [Gerar Bloco = SIM]
- Registro G126 [Gerar Registro = SIM]

![Imagem 3: Na Tela 'Produtos' (Configurações » Cadastros » Produtos) - Aba Bens Sub-Aba CIAP » Geral : Informar o campo 'Data…](https://ajuda.sankhya.com.br/hc/article_attachments/17800067613335) Na Tela 'Produtos' (Configurações » Cadastros » Produtos) - Aba Bens
Sub-Aba CIAP » Geral : Informar o campo **'Data Inicial'.**

![Imagem 4: Na Sub-Aba CIAP - 'Crédito Extemporâneo (Registro G126)':](https://ajuda.sankhya.com.br/hc/article_attachments/17800067623191) Na Sub-Aba CIAP - **'Crédito Extemporâneo (Registro G126)':**

- "**Número da Parcela**" não pode ser maior que "Quantidade de Meses"
- "**Referência p/ Aprop**." não pode ser anterior a "Data Inicial" do CIAP mais o "Número da Parcela"
- "**Referência p/ Aprop**." não pode ser posterior a "Data Final" do CIAP

Através do cenário/parametrizações acima, espera-se que o registro G126 seja devidamente gerado.
