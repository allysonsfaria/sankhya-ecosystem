---
id: "360063013313"
titulo: "Agenda do processamento de XML"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360063013313-Agenda-do-processamento-de-XML"
trilha: "Manual do Produto > Comercial e Vendas > Comercial > Comercial"
atualizado_em: "2026-07-29T14:34:57Z"
rotulos: ["Configuração", "XML", "Agendamento", "Importação", "br.com.sankhya.cac.AgendaProcessamentoXML", "IMPZIPMODFAST", "Agenda do Processamento de XML", "Filtragem de Arquivos: Configuração de filtro para processamento", "EXEROTSUPJOBXML", "Comercial"]
---

# Agenda do processamento de XML

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42312177521943) Módulo: Comercial > Rotinas            ![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42312190678551) Versão disponível: A partir da 4.4
```

---

Por meio desta tela pode-se configurar a frequência em que os arquivos importados pelo Processo de Importação Rápida serão processados, visto que ele importará apenas arquivos e deve ser realizado pela tela [Portal de Importação de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044594354).

![Imagem 3: Por meio desta tela pode-se configurar a frequência em que os arquivos importados pelo Processo de Importação Rápida…](https://ajuda.sankhya.com.br/hc/article_attachments/21452474353431)

Nas abas **"Geral"**, **"Frequência Agendamento"** e **"Horários"** devem ser especificadas as configurações gerais para o agendamento do processamento dos arquivos.

Referente à aba **"Configurações"**, deverão ser preenchidos os campos **"Número de arquivos por processamento"** e **"Intervalo em minutos para execução"** de acordo com suas preferências. No campo **"Configurar filtro"** é possível realizar a inserção de um filtro para que, assim, apenas os arquivos que forem filtrados por ele sejam processados, conforme as definições do agendamento.

Na aba Configurações, ao habilitar o campo **"Processar enquanto houver arquivos"**, o sistema continuará executando automaticamente enquanto houver XMLs pendentes, processando os arquivos em lotes de 50. Nessa condição, o campo de **“Intervalo em minutos para execução"** é desabilitado.

Já com a opção desabilitada, o comportamento do sistema passa a respeitar o agendamento configurado ou os valores preenchidos nos campos de **Intervalo em minutos para execução"** e **"Número de arquivos por processamento"** – sendo que, para este último, um job será disparado para cada quantidade definida.

O campo **"Executar durante horário de faturamento"** possui as seguintes opções:

- **Minutos/Intervalo:** quando essa opção estiver selecionada, a configuração de intervalo será preenchida.
- **Frequência Agendamento:** com essa opção, a aba Frequência Agendamento será preenchida e configurada.

**Observações:**

- **Importar arquivos ZIP pelo modo Rápido? - IMPZIPMODFAST":** ao habilitar este parâmetro, a importação de arquivos ZIP de XML via Portal de Importação será feita de forma otimizada, com os arquivos sendo tratados em lotes de 500, e não individualmente. Após a importação, o processamento dos arquivos seguirá conforme as configurações definidas na tela [Agenda do Processamento de XML](https://ajuda.sankhya.com.br/hc/pt-br/articles/360063013313-Agenda-do-processamento-de-XML).
- Para que toda a rotina superficial dessa tela e do processamento dos XML sejam disparadas para o JOB de execução, é necessário que o parâmetro **"Exec. Rot. superficial Job ProcessamentoXML onSchedule? - EXEROTSUPJOBXML"** esteja ligado, uma vez que **o desligamento desse parâmetro anula a execução do JOB de Processamento de XML**, impedindo que as rotinas automáticas sejam acionadas conforme o agendamento definido.
- Quando o parâmetro **"Converte Xml para UTF-8 na rotina de DFE aut - CONVDFEUTF8"** estiver ligado, ele será capaz de remover caracteres especiais e também remover namespaces que impedem o processamento dos arquivos, além disso, a rotina automática de manifestação irá converter o encoding do texto do XML para UTF-8.

[[voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360063013313-Agenda-do-processamento-de-XML#top)
