---
id: "42951429093399"
titulo: "Configurações - Importar e Exportar"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42951429093399-Configura%C3%A7%C3%B5es-Importar-e-Exportar"
trilha: "ZYDON: Portal de vendas online e pedidos B2B > Geral"
atualizado_em: "2026-08-24T14:02:54Z"
rotulos: ["zydon", "sync_hc", "sync_hash_79804d01b351", "zydon_219372460683"]
---

# Configurações - Importar e Exportar

## Pré-requisitos

- Acesso de Administrador ao Zydon Admin.
- Arquivo de planilha nos formatos .xlsx ou .xls, com até 5 MB.

## Como acessar

No menu lateral, clique em **Configurações → Importar e exportar**.

## Estrutura da tela

À esquerda, fica a lista Todos os tipos, com um campo de busca para localizar rapidamente o tipo de dado desejado (ex.: Produtos, Clientes, Vendedores, Categorias, Descontos). Os tipos que também aceitam exportação exibem a etiqueta Exportável ao lado do nome.

Ao selecionar um tipo, o painel à direita mostra duas abas: Importar e Exportar.

### Aba Importar

- **Envie sua planilha**: arraste o arquivo ou clique na área indicada para selecioná-lo. O mapeamento das colunas é automático.
- **Não tem a planilha?**: clique em **Baixar modelo** para obter a planilha de referência já com as colunas na ordem que o sistema espera para aquele tipo de dado.
- Importações de [tipo]: histórico das importações já realizadas para aquele tipo de dado. Fica vazio até a primeira importação ser feita.

Depois de enviar o arquivo, use o botão **Continuar para mapeamento** (topo da tela) para seguir com o processo de importação

### Aba Exportar

- **Gerar planilha de [tipo**]: exporta todos os registros daquele tipo em .xlsx. Clique em **Exportar [tipo**] para gerar o arquivo — quando ele estiver pronto, aparece na lista abaixo para download.
- **Exportações de [t**ipo]: histórico dos arquivos já exportados, com botão **Atualizar** para verificar se um novo arquivo já ficou pronto.

> Esta exportação traz **todos os registros,** sem filtro. Para exportar só uma parte dos dados, use a tela específica daquele módulo, onde é possível filtrar antes de gerar o arquivo.

**Tipos sem exportação automática:** nem todo tipo de dado tem exportação disponível. Quando não há, a aba Exportar exibe o aviso "Não há exportação automática para [tipo]. A importação por planilha continua disponível na aba Importar." — ou seja, você ainda consegue importar normalmente, só não consegue gerar a planilha de exportação por essa tela.

## Dicas Extras

- Sempre baixe o modelo antes da primeira importação de um tipo de dado — isso evita erros de mapeamento de coluna.
- Para grandes volumes de dados, quebre a planilha em arquivos menores caso ultrapasse o limite de 5 MB.
- Use o histórico de importações/exportações para confirmar se um envio anterior foi concluído antes de repetir a operação.

## Perguntas Frequentes

**Minha planilha não foi aceita, o que pode ter acontecido?**

Confira se o arquivo está no formato .xlsx ou .xls e se o tamanho não excede 5 MB. Também vale a pena baixar o modelo atualizado e comparar a ordem das colunas.

**Consigo exportar só parte dos produtos, como um filtro por categoria?**

Não pela tela de Importar e exportar, que sempre traz todos os registros. Para exportações filtradas, acesse a tela específica do módulo (por exemplo, a tela de Produtos) e gere a exportação a partir de lá.

**Por que não encontro a opção "Exportar" para um determinado tipo de dado?**

Alguns tipos não têm exportação automática disponível. Nesses casos, a aba Exportar avisa que não há exportação para aquele tipo, mas a importação por planilha continua funcionando normalmente.

**Onde consigo ver se minha exportação já ficou pronta?**

Na aba Exportar do tipo de dado, na seção "Exportações de [tipo]". Clique em Atualizar para verificar se o arquivo já está disponível para download.
