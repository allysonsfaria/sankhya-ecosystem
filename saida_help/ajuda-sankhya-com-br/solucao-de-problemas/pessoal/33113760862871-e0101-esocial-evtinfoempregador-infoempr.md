---
id: "33113760862871"
titulo: "E0101[eSocial/evtInfoEmpregador/infoEmpregador/inclusao/infoCadastro/indDesFolha]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33113760862871-E0101-eSocial-evtInfoEmpregador-infoEmpregador-inclusao-infoCadastro-indDesFolha"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:20:07Z"
rotulos: ["Configuração", "Empresa", "Fiscal", "eSocial", "E0101", "Central do eSocial", "E0101[eSocial/evtInfoEmpregador/infoEmpregador/inclusao/infoCadastro/indDesFolha]", "classTrib", "Indicativo de Desoneração", "S-1000"]
---

# E0101[eSocial/evtInfoEmpregador/infoEmpregador/inclusao/infoCadastro/indDesFolha]

**MENSAGEM:**

Ao realizar o processo de envio do evento **S-1000 (**Informações do Empregador/Contribuinte/Órgão Público) o eSocial apresentou a seguinte mensagem:         

E0101[eSocial/evtInfoEmpregador/infoEmpregador/inclusao/infoCadastro/indDesFolha] 

**SOLUÇÃO:**

**(1)** Acesse a tela **"Empresas"** **(Configurações » Cadastros » Empresas)**, aba ''**Informações Fiscais''** e verifique qual opção está selecionada no campo ''**Classificação Tributária''.** E, na aba **"Naturezas"** (desta mesma tela), observe a informação que está preenchida no campo **"Natureza jurídica.** Pois, a configurações desses dois campos terá interferência no passo seguinte. 

**(2)** Em seguida, acesse a outra tela "**Empresas"** **(Configurações» Cadastros» Pessoal» Empresas)** aba ''**Informações Fiscais''** e preencha o campo ''**Indicativo de Desoneração da Folha''** de acordo com as **regras vigentes do eSocial** e conforme a **definições descritas** abaixo:

- **0** - Não aplicável
- **1** - Empresa enquadrada nos critérios da legislação vigente
- **2** - Município enquadrado nos critérios da legislação vigente 
  - **Observação:** o Sankhya não atua com órgãos públicos. Então, apesar do layout do esocial dispor desses 3 itens, o sistema Sankhya apresenta e atua somente com os dois primeiros 0 e 1.

**DEFINIÇÕES:**

- Pode ser igual a [1] apenas se no campo Classificação tributária estiver selecionado: 02, 03, 99;
- Pode ser igual a [2] apenas se no campo Natureza jurídica  estiver igual a: 103-1, 106-6, 124-4, 133-3.
- Os demais casos, deve ser igual a [0].

**(3)** Após realizar os ajustes, **gere novamente o evento S-1000** e **efetue o envio ao eSocial** para validar as correções.

**CAUSA:**

Neste caso, a empresa possui classTrib igual a 99, porém o campo **"Indicativo de Desoneração"** está vazio, o que gera a falha no envio.
