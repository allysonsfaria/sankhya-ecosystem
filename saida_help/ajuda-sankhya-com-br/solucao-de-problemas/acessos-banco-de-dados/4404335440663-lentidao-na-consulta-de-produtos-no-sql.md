---
id: "4404335440663"
titulo: "Lentidão na consulta de produtos no SQL Server, veja como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4404335440663-Lentid%C3%A3o-na-consulta-de-produtos-no-SQL-Server-veja-como-proceder"
trilha: "Solução de Problemas > Acessos/Banco de Dados"
atualizado_em: "2026-07-22T15:23:21Z"
rotulos: ["Produtos", "Configuração", "Atualização", "SQL Server", "#validadoJoaogomes", "Performance", "Correção de lentidão", "Sintaxe SQL", "Consulta de produtos", "Consulta Sintaxe SQL Performance."]
---

# Lentidão na consulta de produtos no SQL Server, veja como proceder

**![Imagem 1: SITUAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16347294030871) SITUAÇÃO:**

O incidente ocorre na tela de consulta de produtos, na qual pode ocorrer a demora para realizar a consulta de cada item. Quando é feita a consulta de produto e é marcado na consulta algum campo tipo varchar ou text, gera uma sintaxe SQL em que ele faz o **REPLACE** (substituição dos caracteres) e o **UPPER** (conversão para maiúsculo) apresenta o incidente descrito abaixo.

![Imagem 2: O incidente ocorre na tela de consulta de produtos, na qual pode ocorrer a demora para realizar a consulta de cada…](https://ajuda.sankhya.com.br/hc/article_attachments/4404335371031)

Quando é realizado uma consulta sem o **REPLACE** e o **UPPER**, não passa pelo filtro e esse tempo gasto para consulta é bastante diminuído.

![Imagem 3: Quando é realizado uma consulta sem o REPLACE e o UPPER , não passa pelo filtro e esse tempo gasto para consulta é…](https://ajuda.sankhya.com.br/hc/article_attachments/4404335395607)

**![Imagem 4: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16347310381975) SOLUÇÃO:**

O incidente está ocorrendo na query principal de consulta de Produtos. Nosso padrão de Collation no SQL Server é CI (Case Insensitive, tanto faz maiúscula e minúscula) e AI (Accent Insensitie, tanto faz com ou sem acentuação). A partir da versão 4.7, na subida do Wildfly, se colocarmos a diretiva: -Dskw.consulta.produtos.sql\_ci\_ai=true, quando a consulta principal de produtos for enviada para o SQL Server, ela já vai sem as tratativas de **UPERCASE** e **REPLACE**.

Para a corrigir tal lentidão, siga os passos abaixo: 

![Imagem 5: Clone o DB de Produção para o ambiente de Testes/Treinamento.](https://ajuda.sankhya.com.br/hc/article_attachments/16347310383255) Clone o DB de Produção para o ambiente de Testes/Treinamento.

![Imagem 6: Aplique a versão 4.7 ou 4.8 nesse ambiente.](https://ajuda.sankhya.com.br/hc/article_attachments/16347310384791) Aplique a versão 4.7 ou 4.8 nesse ambiente.

![Imagem 7: Coloque a diretiva acima na subida do Wildfly.](https://ajuda.sankhya.com.br/hc/article_attachments/16347310386967) Coloque a diretiva acima na subida do Wildfly.

![Imagem 8: Teste a tela de produtos.](https://ajuda.sankhya.com.br/hc/article_attachments/16347294047895) Teste a tela de produtos.

Para mais informações referentes a problemas de performance do sistema, acessar o artigo: [Como analisar os problemas de performance (Lentidão) que ocorrem no sistema ?](https://ajuda.sankhya.com.br/hc/pt-br/articles/360051439534-Como-analisar-os-problemas-de-performance-Lentid%C3%A3o-que-ocorrem-no-sistema-)
