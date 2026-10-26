---
id: "26519455595543"
titulo: "Configurações que impactam no Anexo de Arquivos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/26519455595543-Configura%C3%A7%C3%B5es-que-impactam-no-Anexo-de-Arquivos"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T14:41:34Z"
rotulos: ["Configuração", "Segurança", "Anexos", "Parâmetros", "Passos para resolver", "Razão do erro", "Detalhe do erro", "Configurações que impactam no Anexo de Arquivos", "Armazenamento"]
---

# Configurações que impactam no Anexo de Arquivos

**(1)** Esse artigo tem o objetivo de entender e resolver todos os casos relacionados a funcionalidade de anexar arquivos do sistema.

![Imagem 1: Parâmetros que influenciam no anexo de arquivos:](https://ajuda.sankhya.com.br/hc/article_attachments/26519455587735) Parâmetros que influenciam no anexo de arquivos:

**(1)** **GUARDAANEXOBD - Guardar os anexos no banco de dados**

O parâmetro possibilitará ao usuário salvar os anexos em diretório e não em banco de dados.

**(2)**Se este parâmetro estiver configurado como "Banco de Dados", o sistema guardará os anexos na tabela TSIATA;

**(2)**Se estiver configurado como "Diretório", o sistema armazenará os arquivos no diretório "/SankhyaW/Anexos", e a visualização dos arquivos será possível por meio do Repositório de Arquivos, ou diretamente no servidor de aplicação.

**Observação:** Os arquivos gravados no sistema de arquivos não mantêm seu nome original, ou seja, quando são gravados o sistema gerará para eles um nome único e sem extensão (explicado com mais detalhes no passo 3). Se este diretório ainda não existir, será criado automaticamente pelo sistema.

**IMPORTANTE:** Os anexos vinculados por meio dos botões localizados no cabeçalho das telas legadas são armazenados na tabela **TSIANX** apenas como referência. Nesses casos, o sistema **NÃO** considera o parâmetro "**GUARDAANEXOBD**", e os arquivos são sempre salvos diretamente no repositório de arquivos (ex.: /home/mgeweb/Sistema/Anexos/NomeTela).

**(2)Exemplo de anexo de tela legada:** Cabeçalho da telas como Parceiros, Produtos, Serviços, Telas elaboradas pelo Construtor de telas, entre outras.

Por outro lado, os anexos inseridos através de abas, botões de outras opções ou campos específicos das telas são armazenados na tabela **TSIATA**, e estes sim respeitam o parâmetro "**GUARDAANEXOBD**", podendo ser gravados no banco de dados conforme a configuração definida.

**(2)Exemplo de anexo de tela não legada:** Central de Compras | Vendas | Mov. interna, aba Anexos/Documentos do cadastro de parceiro, entre outras.

**(1)** **SERVANEPOL - Politica de expiração de Anexos em OS**

Responsável por definir os limites de tempo de expiração de acordo com o tamanho do arquivo em bytes.

**Por exemplo:**
Através da configuração "<2:0, <10:15, >10:3", arquivos menores que 2Mb possuem data de expiração livre. Arquivos menores que 10Mb podem expirar em no máximo 15 dias e os maiores que 10Mb podem expirar em no máximo 3 dias.

**Observação:** A configuração do parâmetro só funciona para a opção Anexos das telas, para impressão de notas o sistema sempre vai armazenar anexo no banco de dados, tabela TSIATA.

**(1)** **DIASVENCTFILE - Dias p/ vencimento de arquivos temporários**

Após configurado, apaga arquivos nas seguintes tabelas de acordo com o número de dias inserido.

```
TSIATA.TIPO = 'I'
TMDAMG
TMDAXM
```

**Observação:** em casos de exclusão de arquivos de anexo de e-mail que precisem ser recuperados, a opção é restaurar o backup ou reenviar o e-mail pelas rotinas adequadas do sistema.

![Imagem 2: O Campo "Tipo do Anexo" na TSIATA mostra o valor correspondente a origem do anexo lá inserido. A seguir o valor…](https://ajuda.sankhya.com.br/hc/article_attachments/26519470667287) O Campo **"Tipo do Anexo"** na TSIATA mostra o valor correspondente a origem do anexo lá inserido. A seguir o valor definido para cada um:

- **P -** Parceiro
- **C -** Contrato
- **O -** Ordem de Serviço
- **R -** Produto
- **A -** Agenda Telemarketing
- **N -** Nota
- **F -** Email para formatador de relatório
- **T -** Cotação
- **W -** O.S Web
- **I -** dados de cache para impressão de notas (Por se tratar de dados de cache, podem ser eliminados automaticamente por um job do Sankhya-W ativado pelo parâmetro DIASVENCTFILE)

![Imagem 3: Se ao tentar baixar arquivos da aba Anexo, o sistema apresentar o erro "Arquivo não encontrado". Realize algumas…](https://ajuda.sankhya.com.br/hc/article_attachments/32588743404567) Se ao tentar baixar arquivos da aba Anexo, o sistema apresentar o erro "Arquivo não encontrado". Realize algumas análises.

**(1)** O caminho nos quais os arquivos do **"Repositório de Arquivos"** são salvos fisicamente no servidor é definido pelo parâmetro "FREPBASEFOLDER". Se não está sendo possível realizar o download do arquivo provavelmente ele foi alterado. Por meio da consulta abaixo é possível verificar se houve alteração recente, e quem realizou.

```
SELECT * FROM TSIPARLGT WHERE CHAVE LIKE '%FREPBASEFOLDER%' ORDER BY DHACAO DESC;
```

**(1)**Caso tenha alguma alteração, o caminho se perde e, para corrigir o problema, acesse a pasta original onde o repositório estava apontado, pegue os arquivos e inclua-os na pasta atual do repositório no caminho.

Todos os anexos são salvos no repositório seguindo a lógica:

```
/Sistema/Anexos/$INSTANCIA
```

Exemplos:

```
/Sistema/Anexos/Parceiro
/Sistema/Anexos/Contrato
/Sistema/Anexos/Produto
```

Os arquivos são salvos com um hash em seu nome e sem extensão, então lá terá arquivos do tipo:

```
069da704e5a726366961211cc2c2f6e7
0a24f11577a1209b82fff86125d11bf7
0c8fe173bf678bebbc469c6432bcb2a4
```

**Observação:** devem ser salvos no repositório atual sem modificar **nada.** Do contrário, caso haja modificação, o sistema também perderá o vínculo.
