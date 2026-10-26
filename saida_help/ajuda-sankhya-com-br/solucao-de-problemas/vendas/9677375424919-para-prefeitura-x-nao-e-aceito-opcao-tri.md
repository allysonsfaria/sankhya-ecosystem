---
id: "9677375424919"
titulo: "Para prefeitura X não é aceito opção Tributado em município"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/9677375424919-Para-prefeitura-X-n%C3%A3o-%C3%A9-aceito-op%C3%A7%C3%A3o-Tributado-em-munic%C3%ADpio"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T15:06:41Z"
rotulos: ["Configuração", "Alíquota de ISS", "Impostos", "TOP", "CORE_E03916", "Prefeituras", "NFS-e", "Campo \"Cód. Natureza Oper. ISS\" inválido para a prefeitura de X", "Natureza da operação ISS não definida corretamente", "Ajuste na TOP para selecionar a opção correta; exclua e recrie a nota"]
---

# Para prefeitura X não é aceito opção Tributado em município

**MENSAGEM:**

[CORE\_E03916] Para a prefeitura de X não é aceito a opção "Tributado em município". Altere o campo "Cód. Natureza Oper. ISS (NFS-e)" no cadastro da TOP. Opções aceitas: Exigível; Não incidência; Isenção; Imune/Exportação; Exigibilidade suspensa por decisão judicial; Exigibilidade suspensa por procedimento administrativo.

**CAUSA**:

Não definir a natureza da operação ISS/Município.

**SOLUÇÃO:**

Acesse a tela **Tipo de Operação -TOP** (Caminho de acesso à tela: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP), vá até a aba "Natureza da Operação ISS/Município" e preencha o campo 'Empresa', para que possa ser selecionado uma das opções de Natureza de Operação, por fim, selecione a opção 'Tributado Tomador (tt)'.

Após os ajustes exclua a nota, faça uma nova e transmita-a novamente.

![Imagem 1: Após os ajustes exclua a nota, faça uma nova e transmita-a novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/14500998319383)

A ativação do parâmetro **"Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP"**fará com que a aba **"Natureza da Operação ISS/Município"** seja apresentada no Cadastro de Tipos de Operação - TOP. Isso é feito na tela **Preferências** (Caminho de acesso à tela: Configurações » Avançado » Preferências)

![Imagem 2: A ativação do parâmetro "Utilizar Cód. Nat. Operação ISS por Top/Empresa - NATOPEISSTOPEMP" fará com que a aba…](https://ajuda.sankhya.com.br/hc/article_attachments/14501037070999)
