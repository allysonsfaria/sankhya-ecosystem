---
id: "360049110813"
titulo: "Campo 21 [IND_CENTRALIZADA] da Escrituração Contábil Digital - ECD. Como é gerado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360049110813-Campo-21-IND-CENTRALIZADA-da-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Digital-ECD-Como-%C3%A9-gerado"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:31:34Z"
rotulos: ["Configuração", "Empresa", "ECD", "Fiscal", "avulsa", "Escrituração Descentralizada: IND_CENTRALIZADA valor 1", "Escrituração Centralizada: IND_CENTRALIZADA valor 0", "Campo Empresa Matriz: Define centralização/descentralização", "Escrituração Contábil Digital"]
---

# Campo 21 [IND_CENTRALIZADA] da Escrituração Contábil Digital - ECD. Como é gerado

Na geração da Escrituração Contábil Digital, no Registro 0000 o campo 21 IND\_CENTRALIZADA [Indicador da modalidade de escrituração centralizada ou descentralizada] poderá ser gerado de duas formas:

- 0 – Escrituração Centralizada ou
- 1 – Escrituração Descentralizada

**Quando o sistema vai gerar "1 – Escrituração Descentralizada " ?**

No cadastro da empresa: (Configurações » Cadastros » Empresas) >> Aba Geral > Campo: **"Empresa Matriz":**

- Se este campo "Empresa Matriz",  estiver preenchido e o código for diferente do CODEMP da empresa da geração do ECD, no campo 21 vai gerar 1.
- Se este campo "Empresa Matriz",  estiver preenchido em outro cadastro de empresa, nesta mesma tela, e este seja o código da empresa de geração, o sistema também vai gerar no campo 21 o valor 1.
- Ou seja, se essa empresa tiver alguma  outra empresa como 'Matriz' ou se ela for a 'Matriz' de alguma outra empresa.

**Observação:**

Este campo é novo, sendo exigido a partir do layout 8 [ano calendário 2019, entrega 2020]
