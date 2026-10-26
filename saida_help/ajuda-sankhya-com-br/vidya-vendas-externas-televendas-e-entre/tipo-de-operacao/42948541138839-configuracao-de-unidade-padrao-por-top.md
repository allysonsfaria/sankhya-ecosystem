---
id: "42948541138839"
titulo: "Configuração de unidade padrão por TOP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42948541138839-Configura%C3%A7%C3%A3o-de-unidade-padr%C3%A3o-por-TOP"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Tipo de Operação"
atualizado_em: "2026-08-24T16:42:40Z"
rotulos: ["sync_hc", "vidya", "vidya_476131", "sync_hash_d805ceceefc0"]
---

# Configuração de unidade padrão por TOP

1. Acesse a tela Dicionário de dados e no menu lateral esquerdo, pesquise a tabela TGFTOP e acesse-a.
2. Iremos adicionar 2 campos dentro dessa tabela, o primeiro se encontra dentro da tabela TGFVOL, então, clique em Importar Campo e pesquise por TGFVOL, clique em próximo e ele mostrará o campo que precisamos: **CODVOL**. Altere a descrição do campo para Unidade medida padrão e clique em concluir.
3. O próximo campo que devemos criar é o **AD\_ALTERAUNIDADE**, na tela da TGFTOP clique no ![:plus:](https://ajuda.sankhya.com.br/hc/article_attachments/42956920217111) para adicionar um novo campo, preencha da seguinte forma:
   **Nome do campo:** AD\_ALTERAUNIDADE
   **Descrição do campo:** Bloquear Alterar Unidade Media
   **Tipo de dados:** Texto
   **Apresentação:** Lista de Opções
   **Permite pesquisa:**  Sim
   **Visível no grid de pesquisa:**  Sim
4. Clique nos três pontos (…) no menu acima e selecione Reiniciar esta unidade de dados
5. Na tela de TOP’s, selecione a top desejada e no campo Unidade medida padrão informe a unidade de medida que deseja.

   Caso o campo criado não apareça na tela da TOP verifique se o campo precisa ser adicionado na engrenagem de configurações.
