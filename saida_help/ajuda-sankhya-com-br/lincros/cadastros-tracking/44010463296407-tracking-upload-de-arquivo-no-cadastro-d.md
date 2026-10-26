---
id: "44010463296407"
titulo: "[Tracking] - Upload de Arquivo no Cadastro de Clientes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010463296407--Tracking-Upload-de-Arquivo-no-Cadastro-de-Clientes"
trilha: "Lincros > Tracking > Cadastros - Tracking"
atualizado_em: "2026-10-05T18:38:48Z"
rotulos: ["sync_hc", "lincros", "lincros_16967207", "sync_hash_32262debfdd6"]
---

# [Tracking] - Upload de Arquivo no Cadastro de Clientes

## O que é

O **Upload** permite atualizar o cadastro de vários clientes de uma só vez, através do envio de uma planilha, em vez de editar um por um manualmente. É indicado especialmente para bases com grande volume de clientes.

Essa funcionalidade é diferente da opção **Alteração em massa**, disponível na mesma tela de Clientes. Ambas ficam lado a lado na barra de ações, mas seguem fluxos distintos.

## Pré-requisito

Antes de utilizar essa funcionalidade pela primeira vez, é necessário solicitar ao time Lincros a configuração de um **Layout de Importação** e a ativação da integração **"Serviço de processamento de informações de cliente e ponto de interesse"**. O layout é configurado uma vez para o ambiente e pode (e deve) ser utilizado em todas as Unidades de Negócio, a unidade é escolhida no momento da importação, não faz parte da configuração do layout.

## Passo a passo

1. Acesse **Cadastros > Clientes** e clique no botão **Upload** (na barra de ações, ao lado de Novo, Alteração em massa, Filtros, CSV e Excel).
2. Clique em **Escolher arquivo** e selecione a planilha em Excel (.xlsx) preenchida.
3. Selecione a **UN Negócio** para a qual deseja importar.
4. Selecione o **Layout** que deseja utilizar (caso tenha mais de um configurado).
5. Clique em **Salvar**.

![Imagem 1: Clique em Salvar .](https://ajuda.sankhya.com.br/hc/article_attachments/44010496587415)

## Sobre o arquivo

O arquivo deve ser enviado obrigatoriamente em **Excel (.xlsx)**. Os campos não são identificados pelo nome da coluna, e sim pela **ordem/posição** em que aparecem no arquivo, por isso é fundamental manter exatamente a mesma sequência de colunas do modelo fornecido, como no exemplo abaixo:

![Imagem 2: O arquivo deve ser enviado obrigatoriamente em Excel (.xlsx) . Os campos não são identificados pelo nome da coluna, e…](https://ajuda.sankhya.com.br/hc/article_attachments/44010463769111)

## Observações importantes

- **Endereço:** se as colunas de endereço (Rua, Bairro, Cidade, Estado) forem deixadas em branco, o dado já cadastrado é mantido, ele não é apagado.
- **Telefone:** diferente do endereço, se a coluna de telefone for deixada em branco, o telefone existente **é apagado** do cadastro. Preencha apenas se realmente quiser alterar ou remover o número.
- É possível cadastrar até 3 contatos por cliente, cada um com seu próprio telefone e preferência de SMS.
- Utilize sempre o modelo de planilha fornecido pelo time Lincros, mantendo a mesma ordem de colunas.
