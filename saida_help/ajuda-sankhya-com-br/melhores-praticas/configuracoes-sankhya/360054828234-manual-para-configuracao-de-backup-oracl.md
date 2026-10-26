---
id: "360054828234"
titulo: "Manual para configuração de Backup Oracle Windows"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360054828234-Manual-para-configura%C3%A7%C3%A3o-de-Backup-Oracle-Windows"
trilha: "Melhores Práticas > Configurações Sankhya"
atualizado_em: "2026-07-22T15:28:03Z"
rotulos: ["Configuração", "Agendamento", "Oracle", "Configuração de Backup Oracle Windows", "Windows", "Backup"]
---

# Manual para configuração de Backup Oracle Windows

| - Este manual foi criado para **fornecer as principais orientações na configuração da rotina de Backup do ERP Sankhya** para Banco de Dados Oracle - Windows. - Recomendados que essas orientações **sejam seguidas por um profissional de T.I/banco de dados de sua empresa**, na ausência desse vale ressaltar que em caso de dúvidas ou necessidade de apoio para validar essa configuração, um consultor de serviços de sua Unidade será acionado. |
| --- |

### Imagem 1: Download: Download:

- Execute o download do arquivo em anexo ao final desse artigo;

### Imagem 2: Configuração do Backup (Criando a Pasta): Configuração do Backup (Criando a Pasta):

Descompactar a pasta baixada acima, no disco onde será feito o backup; Neste manual, utilizaremos o **D:** como exemplo.

- Acesse o diretório D:
- Copie e cole o arquivo dentro do D:
- Clique com botão direito, vá na opção “Extrair AQUI”;

### Imagem 3: Agendador de tarefas: Agendador de tarefas:

- Clique na tecla Windows do teclado;
- Pesquise por agendador de Tarefas:

![Imagem 4: Pesquise por agendador de Tarefas:](https://ajuda.sankhya.com.br/hc/article_attachments/19149468539543)

- Clique em **“Biblioteca do agendador”**:

![Imagem 5: Clique em “Biblioteca do agendador” :](https://ajuda.sankhya.com.br/hc/article_attachments/19149494184599)

- No canto direito, clique em **Criar Tarefa**:

![Imagem 6: No canto direito, clique em Criar Tarefa :](https://ajuda.sankhya.com.br/hc/article_attachments/19149468551191)

Será aberta a janela abaixo:

![Imagem 7: Será aberta a janela abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360094883833)

### Imagem 8: Configurando o Agendamento: Configurando o Agendamento:

- Insira na primeira coluna “Nome” o nome do agendamento: "Backup Prod"

![Imagem 9: Insira na primeira coluna “Nome” o nome do agendamento: "Backup Prod"](https://ajuda.sankhya.com.br/hc/article_attachments/19149468562327)

- Clique na aba “Disparadores” e clique em “NOVO...”:

![Imagem 10: Clique na aba “Disparadores” e clique em “NOVO...”:](https://ajuda.sankhya.com.br/hc/article_attachments/19149468566295)

Será aberto a janela abaixo, configure essa tela de acordo com o print abaixo, altere a data para a data atual da criação desse backup:

![Imagem 11: Será aberto a janela abaixo, configure essa tela de acordo com o print abaixo, altere a data para a data atual da…](https://ajuda.sankhya.com.br/hc/article_attachments/19149494212247)

- Após as marcações, clique em OK.

### Imagem 12: Configurando Ações (triggers): Configurando Ações (triggers):

- Clique na aba **Ações** e clique em “NOVO...”:

![Imagem 13: Clique na aba Ações e clique em “NOVO...”:](https://ajuda.sankhya.com.br/hc/article_attachments/19149468588439)

- Será aberto a tela abaixo, clique em 'procurar':

![Imagem 14: Será aberto a tela abaixo, clique em 'procurar':](https://ajuda.sankhya.com.br/hc/article_attachments/19149468593687)

- Selecione o arquivo **“export.bat”**, que está no diretório **D:\backup\scripts**:

![Imagem 15: Selecione o arquivo “export.bat” , que está no diretório D:\backup\scripts :](https://ajuda.sankhya.com.br/hc/article_attachments/360094885013)

- Clique em OK;

| **Importante:**  Agora repita o processo, nomeando as demais execuções para “Backup Full” e “Estatísticas”:  Nome: **Backup FULL** (Aba Geral)   - Diário - Data HOJE - Horario: 19:00 (Aba disparadores) - Caminho: D:\backup\scripts\export\_full.bat (Aba ações)   Nome: **Estatísticas** (Aba Geral)   - Diário - Data HOJE - Horário: 21:00 (Aba disparadores) - Caminho: D:\backup\scripts\estatísticas.bat (Aba ações) |
| --- |

### Imagem 16: Editando os scripts: (Arquivos da pasta "Scripts" - No caso desse artigo: D:/backup/scripts/export_full.bat )Editando os scripts: (Arquivos da pasta "Scripts" - No caso desse artigo: D:/backup/scripts/export\_full.bat)

- Os scripts possuem caminhos pré-definidos, que precisam ser alterados de acordo com o cliente.
- Para editá-los, clique com o botão direito do mouse e clique em “EDITAR”:

![Imagem 17: Ajuste os caminhos de acordo com o que foi configurado:](https://ajuda.sankhya.com.br/hc/article_attachments/360094886033)Ajuste os caminhos de acordo com o que foi configurado:

- Como no nosso exemplo, utilizamos o diretório D:, nota-se acima que ele está direcionado para o C:, logo, precisa ser ajustado.

Para ajustar, basta apagar o caminho errado e substituir pelo correto.

| **Errado** | **Correto** |
| --- | --- |
| SET DIRLOG=C:\backup\logs | SET DIRLOG=D:\backup\logs |
| SET DIREXP=C:\backup\exports | SET DIREXP=D:\backup\exports |

- Clique em Fechar e Salvar.

### Teste:

Para testar, clique duas vezes sobre o arquivo, ele vai apresentar uma tela do CMD, executando o backup. Conforme imagem abaixo:

![Imagem 18: Para testar, clique duas vezes sobre o arquivo, ele vai apresentar uma tela do CMD, executando o backup. Conforme…](https://ajuda.sankhya.com.br/hc/article_attachments/360094886693)

Faça isso para todos os outros arquivos, editando seus caminhos de acordo com o diretório escolhido por você.

### Imagem 19: Conclusão: Conclusão:

- Para concluir, acesse novamente o agendador de tarefas, clique com botão direito em cima de uma das opções que você criou, e clique em EXECUTAR.
- Logo após, acesse o diretório “EXPORTS” dentro do caminho D:\backup e **verifique se gravou o arquivo de backup**, assim como seus logs na pasta LOGS.

**Anexos:**
