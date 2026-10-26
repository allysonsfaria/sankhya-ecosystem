---
id: "37248316961047"
titulo: "Registro D209 - EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37248316961047-Registro-D209-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T14:13:37Z"
rotulos: ["Configuração", "Empresa", "SPED", "Fiscal", "EFD - Escrituração Fiscal Digital", "Impostos", "EFD Contribuições", "Registro D209", "Informações da Suspensão de Exigibilidade dos Tributos", "Parametrizações fiscais", "Processo Admnistrativos Judiciais"]
---

# Registro D209 - EFD Contribuições

Este artigo tem como objetivo apresentar as regras sistêmicas envolvidas na geração do **Registro D209 da EFD Contribuições** no Sankhya.

Serão abordados os principais pontos de atenção relacionados às **parametrizações fiscais**, **cadastros** e **movimentações**, que impactam diretamente a correta composição das informações prestadas ao **SPED**.

#### Procedimento

**(1)** Acesse a tela [**''Empresa''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608254-Empresa) (Comercial » Preferências » Empresa).

**(2)** Na aba **''EFD - Escrituração Fiscal Digital''**, sub-aba **''Blocos e Registros''** verifique se o **Registro D209** está devidamente marcado.

**(3)** Em seguida, acesse a tela [**''Processos Administrativos Judiciais''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044608094-Processos-Administrativos-Judiciais) (Livros Fiscais » Arquivos » Processos Administrativos Judiciais) e localize o processo cadastrado.

**(4)** Na seção **''Configurações EFD Contribuições''** confirme que o campo **''Indicador da Origem do Processo''** esteja configurado como **''1 - Justiça Federal''**.

**(5)** Na aba **''Informações da Suspensão de Exigibilidade dos Tributos''** verifique os seguintes pontos:

- O campo **''Indicativo da Suspensão''** deve estar preenchido e o campo **''% de Suspensão do Imposto''** deve conter um valor, **caso contrário** o campo **''Indicador da Natureza da Ação Judicial''** deve possuir alguma opção selecionada.
- Os campos ''**Dt. Inicial da Vigência''** e ''**Dt. Final da Vigência''** devem abranger o período de geração da **EFD Contribuições**.
- Na sub-aba ''**Impostos''**, no campo **''Tipo de Imposto''** devem estar configurados os tributos ''**PIS/PASEP (EFD – Contribuições)''** e ''**COFINS (EFD – Contribuições)''**.
- As demais subabas possuem preenchimento opcional, conforme a necessidade do cadastro.

O sistema apresentará como **Número do Processo** aquele que possuir a **data mais próxima da geração da EFD** e o **maior valor informado no campo “Nro. do Processo”**, desde que atenda às condições mencionadas anteriormente.
