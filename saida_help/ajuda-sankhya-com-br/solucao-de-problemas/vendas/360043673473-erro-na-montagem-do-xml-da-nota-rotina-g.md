---
id: "360043673473"
titulo: "Erro na montagem do XML da nota. Rotina GerarXMLDaNota. Motivo: Nota Número Único XXXXXX"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043673473-Erro-na-montagem-do-XML-da-nota-Rotina-GerarXMLDaNota-Motivo-Nota-N%C3%BAmero-%C3%9Anico-XXXXXX"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T16:03:40Z"
rotulos: ["#criadoRoger", "#revisadohugo", "Configuração", "NF-e", "XML", "TOP", "Falta arquivo modelo", "Verifique e acesse caminhos corretos", "Caminho ou arquivo inacessível", "Erro", "Documentos Eletrônicos"]
---

# Erro na montagem do XML da nota. Rotina GerarXMLDaNota. Motivo: Nota Número Único XXXXXX

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16120888294167) MENSAGEM:**

Erro na montagem do XML da nota. Rotina GerarXMLDaNota. Motivo: Nota Número Único XXXXXX. O arquivo do modelo "\\hostname\pasta\nomearquivo.txt" não existe!!!

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16120917592727) SOLUÇÃO:**

Para correção, siga os passos abaixo:

![Imagem 3: Acesse Menu » Arquivos » Cadastros » Tipos de Operação:](https://ajuda.sankhya.com.br/hc/article_attachments/16120888302103) Acesse Menu » Arquivos » Cadastros » Tipos de Operação:

(2)** "Modelo de Impressão de nota fiscal"**: Verifique o código informado aqui

(2)** "Modelo para Dados Adicionais de NF-e"**: Verifique o código informado aqui

![Imagem 4: (2) "Modelo para Dados Adicionais de NF-e" : Verifique o código informado aqui](https://ajuda.sankhya.com.br/hc/article_attachments/14629212241431)

![Imagem 5: Acesse: Menu » Avançado » Modelos de Nota Fiscal/Duplicatas/Boletos:](https://ajuda.sankhya.com.br/hc/article_attachments/16120917597975) Acesse: Menu » Avançado » Modelos de Nota Fiscal/Duplicatas/Boletos:

**(2)** Encontre o código que foi verificado no cadastro de TOP.

**(2)** No campo **"Caminho"** do cadastro do modelo, estará o mesmo caminho relatado na mensagem de erro.

![Imagem 6: Este caminho/endereço, deverá estar disponível e acessível na máquina local ou em um diretório compartilhado.](https://ajuda.sankhya.com.br/hc/article_attachments/16120917599255) Este caminho/endereço, deverá estar disponível e acessível na máquina local ou em um diretório compartilhado.

![Imagem 7: Solicite que a Equipe de TI faça as verificações necessárias para que o arquivo e o diretório estejam acessíveis.](https://ajuda.sankhya.com.br/hc/article_attachments/16120917601303) Solicite que a Equipe de TI faça as verificações necessárias para que o arquivo e o diretório estejam acessíveis.

**![Imagem 8: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16120917604119) CAUSA:**

Ocorre quando o arquivo modelo de impressão ou o caminho/diretório não está acessível, geralmente se trata de um diretório compartilhado que pode estar em outro computador e este computador pode estar inacessível (fora da rede interna, desligado).
