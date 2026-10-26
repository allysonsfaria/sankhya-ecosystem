---
id: "39357340584087"
titulo: "Tipo de Operação não existe ou está inativo ou não pode ser usado aqui."
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39357340584087-Tipo-de-Opera%C3%A7%C3%A3o-n%C3%A3o-existe-ou-est%C3%A1-inativo-ou-n%C3%A3o-pode-ser-usado-aqui"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-10-13T17:14:21Z"
rotulos: ["Configuração", "Cache", "Faturamento", "TOP", "Erro", "Artigo criado KCS", "CVE - KCS", "Documentos Eletrônicos"]
---

# Tipo de Operação não existe ou está inativo ou não pode ser usado aqui.

**MENSAGEM**

Tipo de Operação não existe ou está inativo ou não pode ser usado aqui. CORE\_E01315

![Imagem 1: Tipo de Operação não existe ou está inativo ou não pode ser usado aqui. CORE_E01315](https://ajuda.sankhya.com.br/hc/article_attachments/42624523528855)

**SITUAÇÃO**

Esta mensagem aparece ao tentar **"Faturar um pedido"** no sistema, especialmente quando o usuário está realizando um **"Faturamento de pedido para pedido"**, ou ao tentar processar uma operação com um **Tipo de Operação** que não está configurado adequadamente para o fluxo desejado.

**SOLUÇÃO**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse a tela **"Tipos de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e localize o **"TOP"** de origem que está sendo utilizado no faturamento.

**(2)** Clique na aba **"Restrições e Exceções"** dentro do cadastro do **"TOP"**.

**(3)** Configure uma Restrição informando que esta **"TOP"** pode ser usado com o **"TOP"** de destino desejado.

**(4)** Verifique se o **"Tipo de movimento"** da **"TOP"** está configurado corretamente para o fluxo que está sendo executado (exemplo: Pedido para Pedido, Pedido para Nota, etc.).

**(5)** Salve as alterações e tente realizar o faturamento novamente.

**CAUSA**

O erro ocorre porque o fluxo padrão do sistema é de pedido para nota. Quando o usuário tenta realizar um faturamento diferente deste fluxo padrão, como pedido para pedido, é necessário criar uma exceção na configuração do **"TOP"**, informando explicitamente que aquele tipo de operação pode ser usado com o **"TOP"** de destino específico.

Além disso, o erro pode estar relacionado a:

- **"TOP"** inativo ou não cadastrado no sistema.
- **"Tipo de movimento"** incompatível com a operação que está sendo realizada.
- Falta de configuração nas restrições e exceções do **"TOP"**.
- Problemas de cache no navegador que impedem o carregamento correto dos controladores do sistema.
