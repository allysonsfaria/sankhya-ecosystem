---
id: "360045640054"
titulo: "'Campo Obrigatório' COD_CTA Código da conta analítica de contabilização do bem ou componente (campo 06 do Registro 0500)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045640054--Campo-Obrigat%C3%B3rio-COD-CTA-C%C3%B3digo-da-conta-anal%C3%ADtica-de-contabiliza%C3%A7%C3%A3o-do-bem-ou-componente-campo-06-do-Registro-0500"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T15:32:46Z"
rotulos: ["#criadoRoger", "Configuração", "Fiscal", "Contas", "Impostos", "Preferências", "#AGUARDANDOVALIDAÇÃO", "Conta contábil ausente", "Vincule conta corretamente", "Campo Obrigatório", "EFD Contribuições"]
---

# 'Campo Obrigatório' COD_CTA Código da conta analítica de contabilização do bem ou componente (campo 06 do Registro 0500)

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/18604435012887)MENSAGEM**:

'Campo Obrigatório' COD\_CTA Código da conta analítica de contabilização do bem ou
componente (campo 06 do Registro 0500).

**![Imagem 2: CAUSA :](https://ajuda.sankhya.com.br/hc/article_attachments/18604435021847) CAUSA**:

 Ocorre quando a empresa gera as contas no EFD contribuições pelos cadastros, e a  Conta Contábil do cadastro do **(bem)** Imobilizado não esta devidamente informada.

**![Imagem 3: SOLUÇÃO :](https://ajuda.sankhya.com.br/hc/article_attachments/18604435028119) SOLUÇÃO**:

![Imagem 4: Acesse o Preferencias de Empresa em (Comercial » Preferências » Empresa) Aba: EFD-Escrituração Fiscal Digital Tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/18604424453143) Acesse o Preferencias de Empresa em (Comercial » Preferências » Empresa)
Aba: EFD-Escrituração Fiscal Digital
Tipo de Escrituração = EFD Contribuições
Campo: Tipo da conta contábil para EFD = [Cadastros]

![Imagem 5: Vincule a conta em um dos cadastros das seguintes telas, que obedece a mesma sequência hierárquica aqui listada:](https://ajuda.sankhya.com.br/hc/article_attachments/18604424459927) Vincule a conta em um dos cadastros das seguintes telas, que obedece a mesma sequência hierárquica aqui listada:

2.1-Cadastro de Produtos (Configurações » Cadastros » Produtos » Produtos)
Aba: Impostos ou Impostos/Informações por empresa
Campo: Conta contábil para EFD

2.2-Cadastro de Serviço (Configurações » Cadastros » Produtos » Serviço)
Aba: Impostos ou Configuração por empresa
Campo: Conta contábil para EFD

2.3-Cadastro de Grupo de Produto/Serviços (Configurações » Cadastros » Produtos » Grupos de Produtos/Serviços)
Aba: Impostos por empresa
Campo: Conta contábil para EFD
2.4-Cadastro de Natureza (Configurações » Cadastros » Gerencial » Natureza de Receitas e Despesas)
Aba: PIS/COFINS Todas a empresas
Campo: Conta contábil para EFD2.5-Cadastro de TOP (Comercial » Arquivo » Cadastros » Tipos de Operação - TOP)
Aba: Impostos
Campo: Conta contábil para EFD

![Imagem 6: Verifique se a conta que esta vinculada em uma das telas do passo 2. Está com o campo "Natureza para EFD:" Preenchido,…](https://ajuda.sankhya.com.br/hc/article_attachments/18604435062807) Verifique se a conta que esta vinculada em uma das telas do passo 2.
Está com o campo "Natureza para EFD:" Preenchido, na tela: Plano de Contas
(Livros Fiscais » Contabilidade » Plano de Contas), aba Geral.
