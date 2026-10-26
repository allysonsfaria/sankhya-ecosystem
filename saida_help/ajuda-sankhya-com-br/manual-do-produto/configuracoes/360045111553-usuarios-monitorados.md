---
id: "360045111553"
titulo: "Usuários Monitorados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045111553-Usu%C3%A1rios-Monitorados"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:57:59Z"
rotulos: ["manual", "Configuração", "WMS", "Monitoramento", "br.com.sankhya.cfg.usuarios.monitorados", "Usuários Monitorados manual", "Performance", "Análise de performance", "Monitoramento de tarefas", "Ferramenta de acompanhamento", "Logs"]
---

# Usuários Monitorados

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310970041879) Módulo: Configurações > Avançado
```

---

Utiliza-se esta tela como uma ferramenta de acompanhamento das tarefas que forem executadas no Coletor WMS e no [Sankhya OK](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045229434). Estas tarefas passarão por uma análise de performance, que servirão para verificação de possíveis erros não casuais.

![Imagem 2: Utiliza-se esta tela como uma ferramenta de acompanhamento das tarefas que forem executadas no Coletor WMS e no Sankhya…](https://ajuda.sankhya.com.br/hc/article_attachments/13349607555863)

Deve-se selecionar no campo **"Cód. Usuário"** o usuário que será monitorado e informar no campo **"Data da Expiração"** uma data superior a data atual, pois esta data determinará o término do período ao qual o usuário estará sendo monitorado.

Ao executar as tarefas pelo Coletor WMS ou Sankhya OK, o sistema irá gerar logs para análise de performance enquanto as tarefas estiverem sendo executadas, até a data informada.

**Observação:** no parâmetro **"Diretório base para o repositório de arquivos - FREPBASEFOLDER"** é possível inserir o caminho da pasta destino dos logs gerados.

Serão gerados dois arquivos no diretório C:\Users\usuário do Windows\sw-logs\sqlmon, sendo eles:

- Um arquivo com as consultas executadas no banco de dados;
- Um arquivo contendo as funções que foram utilizadas no Sankhya Om.
