---
id: "39383297795735"
titulo: "Tela de Identificação do Cliente Incompleta no Sankhya Checkout"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39383297795735-Tela-de-Identifica%C3%A7%C3%A3o-do-Cliente-Incompleta-no-Sankhya-Checkout"
trilha: "Dúvidas Frequentes > Varejo"
atualizado_em: "2026-07-22T13:32:00Z"
rotulos: ["Produtos", "Configuração", "Parceiro", "Nota Fiscal", "Sankhya Checkout", "Erro", "Artigo criado KCS", "Varejo - KCS"]
---

# Tela de Identificação do Cliente Incompleta no Sankhya Checkout

**Situação**

Ao realizar a venda ou troca de produtos no checkout, a tela **“Identificação do Cliente”** não apresenta todos os campos necessários para o correto processamento das informações.

Essa inconsistência impede a visualização completa dos dados do cliente e acaba comprometendo a emissão da nota de troca no sistema Sankhya.

Tela de identificação exibida incorretamente ao realizar troca no Checkout:

![Imagem 1: Tela de identificação exibida incorretamente ao realizar troca no Checkout:](https://ajuda.sankhya.com.br/hc/article_attachments/39570395473559)

**Solução**

Para resolver o problema, siga os passos abaixo:

**(1)** Acesse a tela **"Cadastro de Checkout"** (Menu >>  Cadastros >> Checkouts).
**(2)** Localize e selecione o PDV específico a ser ajustado, e abra o cadastro com duplo clique.
**(3)** Na aba Preferencias >> marque o campo **"Integrar Parceiros"** para habilitar a integração.

![Imagem 2: Salve as alterações realizadas no cadastro.](https://ajuda.sankhya.com.br/hc/article_attachments/39570395475991)
**(4)** Salve as alterações realizadas no cadastro.

**(5)** Realize um novo teste no PDV para validar que a tela **"Identificação do Cliente"** está sendo exibida completamente.

Ao Seguir o passo a passo a tela **''Identificação do Cliente''** deve ser apresentada da seguinte maneira:

![Imagem 3: Ao Seguir o passo a passo a tela ''Identificação do Cliente'' deve ser apresentada da seguinte maneira:](https://ajuda.sankhya.com.br/hc/article_attachments/39570395477271)

**Causa**

O problema ocorre porque o campo **"Integrar Parceiros"** não estava marcado no cadastro do checkout do PDV específico. Essa configuração é essencial para a exibição completa da tela de identificação do cliente, pois permite a integração completa dos dados dos parceiros com o sistema.

Sem essa marcação, o sistema não consegue carregar todas as informações necessárias para processar corretamente a operação de troca e emitir a nota fiscal correspondente.
