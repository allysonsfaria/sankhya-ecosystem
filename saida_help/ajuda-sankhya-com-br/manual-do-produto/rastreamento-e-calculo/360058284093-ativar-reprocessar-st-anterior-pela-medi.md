---
id: "360058284093"
titulo: "Ativar/Reprocessar ST Anterior pela Média das Entradas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360058284093-Ativar-Reprocessar-ST-Anterior-pela-M%C3%A9dia-das-Entradas"
trilha: "Manual do Produto > Fiscal e Contábil > Fiscal > Substituição Tributária  > Rastreamento e cálculo"
atualizado_em: "2026-09-15T17:25:12Z"
rotulos: ["Configuração", "Livros Fiscais", "Impostos", "Estoque", "Preferências", "br.com.sankhya.mgeliv.ProcessarSTAnteriorPorMedia", "Seleção empresa e produtos", "Processamento de ICMS-ST", "Histórico e configurações", "ICMS-ST"]
---

# Ativar/Reprocessar ST Anterior pela Média das Entradas

| ``` ![Imagem 1: Módulo: Livros Fiscais > Avançado > Apuração ICMS-ST por média Versão disponível: A partir da 4.5](https://ajuda.sankhya.com.br/hc/article_attachments/42313138332055) Módulo: Livros Fiscais > Avançado > Apuração ICMS-ST por média   ![Imagem 2: Módulo: Livros Fiscais > Avançado > Apuração ICMS-ST por média Versão disponível: A partir da 4.5](https://ajuda.sankhya.com.br/hc/article_attachments/42313108229015) Versão disponível: A partir da 4.5 ``` |
| --- |

---

![Imagem 3: Esta tela será utilizada para a seleção da empresa e produtos que deverão ser marcados para indicar os valores BC ST e…](https://ajuda.sankhya.com.br/hc/article_attachments/16255830892311) Esta tela será utilizada para a seleção da empresa e produtos que deverão ser marcados para indicar os valores BC ST e ICMS ST contemplando o valor unitário médio das bases de cálculo da retenção apurado no mês anterior ao da saída considerando todas as aquisições no período requerido.

---

Inicialmente no **"Painel de Filtros"**, além dos filtros usuais do sistema, você pode selecionar na seção **"Preferências"**, campo **"Opções"**, a forma que será realizado o processamento, isto é, com base na **"Cópia de Estoque"**, **"Contagem de Estoque"**, ou se desejar, você também pode **"Apenas marcar"** os produtos sem que os cálculos sejam realizados.

Depois, em **"Marcar Implantação"**, escolha entre as opções **"Tabela de Produtos"** e **"Tabelas de Produtos por Empresas"**.

Por fim, preencha o campo **"Data da Cópia/Contagem"**, com a data que você deseja filtrar e clique em **"Aplicar"**.

![Imagem 4: Por fim, preencha o campo "Data da Cópia/Contagem" , com a data que você deseja filtrar e clique em "Aplicar" .](https://ajuda.sankhya.com.br/hc/article_attachments/7885974700567)

**Observação:** por meio do parâmetro **"Data limite mínima para buscar notas de entrada. - DTMINGETENTRAST"** você poderá definir a data limite mínima para as buscas das notas de entrada no sistema.

Na aba **"Dados para Ativar a Implantação"**, serão apresentados os dados das **"Empresas"** e **"Produtos"** que poderão ser utilizados na implantação.

![Imagem 5: Na aba "Dados para Ativar a Implantação" , serão apresentados os dados das "Empresas" e "Produtos" que poderão ser…](https://ajuda.sankhya.com.br/hc/article_attachments/7886215756567)

Já na aba **"Produtos com Problemas na Implantação"** será exibido aqueles produtos com algum tipo de erro durante a execução do processamento da implementação.

![Imagem 6: Já na aba "Produtos com Problemas na Implantação" será exibido aqueles produtos com algum tipo de erro durante a…](https://ajuda.sankhya.com.br/hc/article_attachments/7886318836887)

Por meio do botão ![Imagem 7: Por meio do botão "Processar/Ativar" você irá realizar o processamento do(s) produto(s) / empresa(s) que foram…](https://ajuda.sankhya.com.br/hc/article_attachments/7885970975511) **"Processar/Ativar"** você irá realizar o processamento do(s) produto(s) / empresa(s) que foram requeridos pelos filtros.

Tem-se ainda que por meio do botão ![Imagem 8: Tem-se ainda que por meio do botão "Histórico" você poderá consultar o histórico dos processamentos realizados na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/7886023852951) **"Histórico"** você poderá consultar o histórico dos processamentos realizados na tela:

[GIF animado: Imagem 9: Tem-se ainda que por meio do botão "Histórico" você poderá consultar o histórico dos processamentos realizados na tela:](https://ajuda.sankhya.com.br/hc/article_attachments/7886787463703)

Após o processamento, os valores que compõem as tags <**vBCSTret**> e <**vICMSSTret**> serão recebidas com o valor unitário médio das bases de cálculo da retenção apurado no mês anterior e se a marcação **"Obtém ST Anterior pela média das entradas?"** (tela **"Preferências da Empresa"**, aba [Livros Fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#abalivrosfiscais)) estiver acionada.

**Nota:** você pode utilizar o parâmetro **"Tops a serem utilizadas na apuração de st anterior por média - TOPAPURSTANTMED"** para definir as TOP's que não movimentam Livros Fiscais e participarão do processo de apuração.

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058284093-Ativar-Reprocessar-ST-Anterior-pela-M%C3%A9dia-das-Entradas#top)
