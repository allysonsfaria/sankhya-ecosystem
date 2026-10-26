---
id: "360045108733"
titulo: "Monitor de Consultas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045108733-Monitor-de-Consultas"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-10-19T19:12:12Z"
rotulos: ["manual", "SQL", "Configuração", "Relatórios", "Monitor", "Monitor de Consultas", "Queries", "Stracktraces", "br.com.sankhya.cfg.monitordeconsultas", "Monitor de Consultas manual", "Arquivos", "Monitoramento", "Log", "Monitor de Consultas para Logs"]
---

# Monitor de Consultas

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42310884956439) Módulo: Configurações > Avançado
```

---

O Monitor de Consultas permitirá que você realize a geração de arquivos de log das querys e stacktraces (processos) das telas e também, faça o download dos mesmos. Essa funcionalidade é equivalente ao SQLMon, utilizado para gerar log do MGE/Jiva G1.

Essa tela não possui controle de acessos, ou seja, todos que utilizam nosso sistema poderão utilizá-la.

Para se trabalhar com essa tela é bem simples, basta dar apenas um clique no botão ![Imagem 2: Para se trabalhar com essa tela é bem simples, basta dar apenas um clique no botão "Iniciar monitoramento" , para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/15632916385047) **"Iniciar monitoramento"**, para que o monitoramento seja iniciado.

![Imagem 3: Para se trabalhar com essa tela é bem simples, basta dar apenas um clique no botão "Iniciar monitoramento" , para que o…](https://ajuda.sankhya.com.br/hc/article_attachments/360075371914)

Finalizada a navegação nas rotinas desejadas, para interromper o monitoramento, clique no botão ![Imagem 4: Finalizada a navegação nas rotinas desejadas, para interromper o monitoramento, clique no botão "Parar monitoramento" .](https://ajuda.sankhya.com.br/hc/article_attachments/15632976623127) **"Parar monitoramento"**.

Quando desejar obter os arquivos de log gerados, basta paralisar a gravação e clicar no botão **"Baixar arquivos de Log"**:

![Imagem 5: Quando desejar obter os arquivos de log gerados, basta paralisar a gravação e clicar no botão "Baixar arquivos de Log" :](https://ajuda.sankhya.com.br/hc/article_attachments/360076541053)

Só é possível Baixar o arquivo de Log se o monitoramento estiver Parado.

**Dados informados nos arquivos**

Log do SQL

**##ID\_x##**: É um identificador para relacionar a query com o seu respectivo stackTrace;

**Tempo**: É o tempo de execução da query;

**Query**: Query executada no sistema;

**Params**: Os parâmetros que a query está utilizando.

Abaixo, trouxemos um exemplo de logs de queries gerados:

![Imagem 6: Abaixo, trouxemos um exemplo de logs de queries gerados:](https://ajuda.sankhya.com.br/hc/article_attachments/360076541133)

Log do stackTrace

**##ID\_x##**: Identificador que relaciona o stackTrace com a sua respectiva query.

Agora um exemplo de logs de stackTraces gerados:

![Imagem 7: Agora um exemplo de logs de stackTraces gerados:](https://ajuda.sankhya.com.br/hc/article_attachments/360076541173)

Os nomes dos arquivos serão:

- Do arquivo zip será Monitoramento.zip;
- O arquivo com as querys efetuadas pelo sistema terá o nome de Monitor\_Consultas.log;
- Staktraces (processos) será denominado Monitor\_Processos.log.

**Mensagens de erro**

As mensagens de erro estarão presentes no arquivo Monitor\_Processos; no arquivo Monitor\_Consultas serão somente informações do Banco de Dados.

**Observação:** o arquivo Monitor\_Consultas.log trará os dados utilizados para efetuar a query. Exemplo: SELECT \* FROM TGFPAR WHERE CODPARC=?; posteriormente, trará o argumento 1=10, ou seja, o código do parceiro informado para fazer o select é o número 10.
