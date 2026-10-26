---
id: "43548953488535"
titulo: "Quais configurações e boas práticas garantem o correto funcionamento das rotinas de caixa no PDV Web!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43548953488535-Quais-configura%C3%A7%C3%B5es-e-boas-pr%C3%A1ticas-garantem-o-correto-funcionamento-das-rotinas-de-caixa-no-PDV-Web"
trilha: "Melhores Práticas > Varejo"
atualizado_em: "2026-10-07T19:26:06Z"
rotulos: ["Artigo criado KCS", "Varejo - KCS"]
---

# Quais configurações e boas práticas garantem o correto funcionamento das rotinas de caixa no PDV Web!

O correto funcionamento das rotinas de **Abertura de caixa**, **Vendas** e **Sangria/Suprimento** no **PDV Web** depende de configurações adequadas, permissões de acesso e do cumprimento dos procedimentos operacionais definidos pela empresa.

Falhas ou inconsistências nessas rotinas podem comprometer o controle financeiro, gerar divergências entre os valores registrados e o saldo físico do caixa e impactar a operação da loja.

Este artigo apresenta as principais configurações, boas práticas e procedimentos para identificar e evitar problemas nas operações de caixa, proporcionando maior segurança, controle e rastreabilidade.

#### **(1)**Configurações essenciais para o PDV Web

Para garantir que as rotinas de abertura de caixa, vendas e sangria/suprimento funcionem corretamente, valide as seguintes configurações:

Certifique-se de que o acesso à tela **Portal de Caixa** esteja liberado para os usuários necessários na rotina **Acessos** (**Configurações » Controle de Acesso » Acessos**).

 Na tela **Usuários** (**Configurações » Controle de Acesso » Usuários**), verifique se o perfil do usuário está corretamente configurado, especialmente nas abas **PDV Web** e **Segurança**, liberando as rotinas de **Abertura de caixa**, **Fechamento de caixa**, **Sangria** e **Suprimento**.

 No **Configurador de Layout da Nota** (**Comercial » Configuração » Configurador de Layout da Nota**), marque a opção **Usar PDV Web** para os tipos de movimento utilizados nas operações de venda.

 Defina corretamente o **Tipo de Recebimento** na aba **Preferências PDV Web** do **Configurador de Layout da Nota**.

 Valide os parâmetros relacionados ao caixa, especialmente o parâmetro **Gerar sangria ao fechar caixa - GERSANGSALDOCX**, que, quando habilitado, realiza automaticamente a **sangria do saldo do caixa no momento do fechamento**.

A configuração desses parâmetros deve estar alinhada às regras operacionais e financeiras adotadas pela empresa.

#### **(1)**Boas práticas para abertura de caixa, vendas e sangria

Adote as seguintes práticas para garantir o correto funcionamento das rotinas:

Realize a **Abertura de caixa** sempre no início do expediente, registrando o valor do suprimento inicial (troco) por meio do botão **Suprimento**, quando necessário.

 Efetue as **Vendas** normalmente, conferindo os valores informados e as formas de pagamento. Utilize a coluna **Informado** para registrar os valores recebidos no momento de fechar o caixa na tela de PDV web.

 Realize a **Sangria** sempre que o valor em dinheiro no caixa atingir o limite definido pela empresa, utilizando o botão **Sangria** e preenchendo corretamente os campos obrigatórios.

 No fechamento do caixa, confira todos os valores registrados, utilize o relatório de conferência e imprima o comprovante para assinatura do operador e do gestor.

**Atenção:** quando o parâmetro **GERSANGSALDOCX** estiver habilitado, a sangria do saldo do caixa será realizada automaticamente no fechamento. Nesse cenário, considere esse comportamento ao definir o procedimento de conferência e fechamento do caixa.

Evite realizar sangrias ou suprimentos fora dos procedimentos estabelecidos, pois operações não registradas corretamente podem provocar divergências entre o saldo físico e o saldo apresentado pelo sistema

###
