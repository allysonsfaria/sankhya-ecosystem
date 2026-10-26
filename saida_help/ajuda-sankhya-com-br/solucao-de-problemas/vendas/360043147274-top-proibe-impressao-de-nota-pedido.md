---
id: "360043147274"
titulo: "TOP proíbe impressão de Nota/Pedido"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043147274-TOP-pro%C3%ADbe-impress%C3%A3o-de-Nota-Pedido"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-31T04:17:55Z"
rotulos: ["Configuração", "Impressão", "TOP", "Altere opção \"Imprimir\" na TOP", "TOP proíbe impressão de documento", "TOP bloqueia impressão", "Artigo atualizado KCS", "CVE - KCS", "Comercial"]
---

# TOP proíbe impressão de Nota/Pedido

**Mensagem**

Documento X: TOP proíbe impressão de Nota/Pedido.

**Solução**

**(1)** Acesse **Comercial >> Cadastros >> Tipos de Operação (TOP)**.

**(2)** Selecione a TOP usada no documento e vá até a aba **Impressão**. 

**(3)** Altere o campo **Imprimir** para uma das opções que permitem impressão:

- **Manual -** impressão sob demanda, quando o usuário solicitar.
- **Opcional** - o sistema pergunta se deseja imprimir.
- **Na Confirmação** - impressão automática ao confirmar o documento.

**(4)** Salve a alteração.

![Imagem da tela de impressão](https://ajuda.sankhya.com.br/hc/article_attachments/14658005059607)

**Causa**

O Tipo de Operação (TOP) usado no documento está com o campo **Imprimir** configurado como **Proibido**, o que impede a impressão da nota ou do pedido.

**Importante:** o campo Imprimir é um dado **histórico,** seu valor é gravado no documento no momento em que ele é criado/confirmado. Alterar a TOP não libera a impressão de documentos já existentes; é necessário emitir um **novo** documento para que a mudança tenha efeito.
