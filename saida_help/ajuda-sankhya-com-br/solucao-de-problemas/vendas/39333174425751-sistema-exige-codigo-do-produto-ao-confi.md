---
id: "39333174425751"
titulo: "Sistema exige código do produto ao configurar desconto por grupo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39333174425751-Sistema-exige-c%C3%B3digo-do-produto-ao-configurar-desconto-por-grupo"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-08-31T02:37:21Z"
rotulos: ["Produtos", "Configuração", "Cadastro", "Erro", "Artigo criado KCS", "CVE - KCS", "Desconto Promocional"]
---

# Sistema exige código do produto ao configurar desconto por grupo

**Mensagem**

**Produto não existe ou está inativo ou não pode ser usado aqui.** **CORE\_E01315**

O sistema não permite concluir a criação do desconto promocional, exigindo que o código do produto seja preenchido, mesmo quando a opção de desconto por grupo está selecionada.

**Situação**

Ao tentar configurar um desconto promocional por grupo de desconto, o usuário cria o grupo de desconto de produto e o atribui ao desconto. Porém, ao tentar concluir a criação, o sistema bloqueia a operação exigindo o preenchimento do campo **"Código do Produto"**. Como a opção selecionada é desconto por grupo, o sistema não permite informar o código do produto individualmente, o que faz sentido, já que o desconto deveria ser aplicado a todos os produtos do grupo.

**Solução**

Para corrigir o comportamento, realize o cadastro do produto de código **0** (zero) na base de dados:

**(1)** Acesse a tela **"Produtos"** (Comercial Arquivo Cadastros Produtos).

**(2)** Crie um novo produto com o código **0**.

**(3)** Preencha os campos obrigatórios do cadastro do produto.

**(4)** Salve o cadastro do produto.

**(5)** Retorne à tela **"Descontos Promocionais"** (Comercial Avançado Descontos Promocionais) e configure novamente o desconto por grupo.

Após a criação do produto de código **0**, o sistema permitirá a conclusão da configuração do desconto promocional por grupo normalmente.

**Causa**

O comportamento ocorre porque o sistema realiza uma validação interna que requer a existência do produto de código **0** na base de dados para processar corretamente os descontos promocionais por grupo. Quando este produto não existe no ambiente, o sistema não consegue concluir a rotina de criação do desconto, exigindo incorretamente o preenchimento do campo Código do Produto.
