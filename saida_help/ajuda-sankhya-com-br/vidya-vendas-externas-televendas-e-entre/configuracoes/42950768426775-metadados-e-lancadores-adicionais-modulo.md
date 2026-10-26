---
id: "42950768426775"
titulo: "Metadados e Lançadores Adicionais — Módulo Vidya Force (Sankhya)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950768426775-Metadados-e-Lan%C3%A7adores-Adicionais-M%C3%B3dulo-Vidya-Force-Sankhya"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Configurações"
atualizado_em: "2026-08-24T16:11:28Z"
rotulos: ["sync_hc", "vidya", "vidya_600117", "sync_hash_6041bcec19f9"]
---

# Metadados e Lançadores Adicionais — Módulo Vidya Force (Sankhya)

## Metadados: <https://drive.google.com/drive/u/0/folders/1XvZwI6W3TcJ4gWlYc6zDo_UUms-vzto7> 1. O que são os "Metadados" no Sankhya

No Sankhya, os **Metadados** são a definição estrutural de uma tela/entidade do sistema: quais tabelas ela usa, quais campos existem, tipos de dado, chaves primárias, relacionamentos entre tabelas, opções de combo, regras de exibição, etc. Quando um módulo customizado (como o Vidya Force) é desenvolvido, essa estrutura é exportada em um arquivo `metadata.xml`, que pode ser importado em qualquer ambiente Sankhya para recriar as telas correspondentes sem precisar remontá-las manualmente campo a campo.

Um pacote de metadados pode vir acompanhado de arquivos `.JAR` — como é o caso do pacote analisado, que traz o `VIDYAUPDATESETTINGSCACHEEVENT.JAR`. Esse tipo de arquivo contém listeners/eventos Java que rodam nos bastidores (por exemplo, atualizando o cache de configurações automaticamente quando um registro da tabela de configuração é alterado), e precisam estar presentes na pasta indicada para o metadado funcionar corretamente.

## 2. Análise do pacote `Metadados_AD_TVDYCFGFRC (exemplo)`

O arquivo `metadata.xml` analisado traz a exportação completa da tela de **Configurações — Vidya Force** (`AD_TVDYCFGFRC`) e de todas as entidades relacionadas a ela. Ao todo, o pacote contém **21 tabelas/instâncias** do módulo Vidya:

| Tabela | Descrição |
| --- | --- |
| `AD_TVDYCFGFRC` | Configurações Vidya Force (tabela principal) |
| `AD_TVDYCFGCAD` | Configuração de Cadastro |
| `AD_TVDYFXRENT` | Faixa de Rentabilidade |
| `AD_TVDYFRCSTS` | Status Vidya Force |
| `AD_TVDYGRUOP` / `AD_TVDYTOPGRU` | Grupo de Operação / Grupo de Vendedores |
| `AD_TVDYLYTTOP` | Layout por TOP (Tipo de Operação) |
| `AD_TVDYMOBTOP` | Configuração de mobilidade por Tipo de Operação |
| `AD_TVDYPRODEST` | Produtos por Estabelecimento |
| `AD_TVDYPRODPERF` | Produtos por Performance |
| `AD_TVDYPRODSPERFIL` | Produtos por Perfil |
| `AD_TVDYRFE` | Configuração de RFE |
| `AD_TVDYUSUMASTER` | Usuário Master |
| `AD_TVDYCAMPAR` / `AD_TVDYCAMPRO` | Campanhas |
| `AD_TVDYLNKUTL` | Link Utilitário |
| `AD_VVDYMOBEMP`, `AD_VVDYMOBLOC`, `AD_VVDYMOBNTA`, `AD_VVDYMOBPRO`, `AD_VVDYMOBTIPVENDA` | Views de apoio à mobilidade (empresa, local, nota, produto, tipo de venda) |

O bloco `dbMetadata` do XML registra de qual banco o metadado foi exportado — no caso analisado, um banco **Oracle 19c**, com driver JDBC Oracle. É esse mesmo bloco que muda quando o metadado é gerado a partir de um ambiente **SQL Server**.

## 3. Diferença entre o pacote Oracle e o pacote SQL Server

Apesar de a estrutura lógica das telas (campos, relacionamentos, regras) ser a mesma, o Sankhya disponibiliza pacotes de metadados **separados por engine de banco** pelos seguintes motivos:

- **Origem registrada no XML**: o cabeçalho `exportInfo > dbMetadata` grava o usuário do banco, a string de conexão JDBC, o driver e a versão do SGBD de onde o metadado foi exportado (Oracle Database ou SQL Server). Isso serve tanto de rastreabilidade quanto de validação na hora da importação.
- **Compatibilidade de tipos de dado e geração de chave**: Oracle e SQL Server têm formas distintas de gerar sequência/autoincremento (sequences no Oracle vs. `IDENTITY` no SQL Server) e pequenas diferenças de mapeamento de tipos (`NUMBER` vs. `INT/DECIMAL`, `VARCHAR2` vs. `VARCHAR`, por exemplo). O metadado exportado de cada engine já reflete essas particularidades da tabela física correspondente.
- **Script de criação das tabelas físicas**: antes de importar o metadado, as tabelas físicas (`AD_TVDY...`) precisam existir no banco de dados-alvo. Por isso normalmente existe um script de criação de tabela específico para Oracle e outro para SQL Server, seguindo a sintaxe de cada SGBD — e o metadado correspondente deve ser aplicado sobre o banco do mesmo tipo.

## 4. Como importar os Metadados

1. Acesse o **Navegador Sankhya**.
2. Vá em **Construtor de Telas**.
3. Clique em **Outras Opções (▼)**.
4. Selecione **Metadados** → **Importar Metadados**.
5. Localize e selecione o arquivo de metadados correspondente ao banco do ambiente (Oracle ou SQL), a partir da pasta `\Vidya\querys-vidya-force\...`, seguindo a estrutura de subpastas referente ao banco em questão.
6. Confirme a importação.

> **Importante**: sempre importe o Metadados **primeiro** e, em seguida, já crie o Lançador correspondente àquela tela, na mesma sequência — evita esquecer o lançador e deixar a tela sem acesso pelo menu.

## 5. Como criar os Lançadores

1. No **Navegador Sankhya**, vá em **Construtor de Telas**.
2. Clique em **Outras Opções (▼)**.
3. Selecione **Lançadores** → **Adicionar Lançador**.
4. Digite o nome do lançador (deve ser o mesmo nome/código da tela recém-importada).
5. Selecione a pasta **Comercial** como destino do lançador.
6. Salve.

### Regra geral: o lançador deve sempre ser criado apontando para a tela de mesmo código/nome do metadado recém-importado, exceto nos casos explicitamente marcados como dispensados (integrações `AD_INTBANDVIDYA` e `AD_INTCARDVIDYA`, que não possuem tela de navegação própria).

## 6. Resumo do fluxo completo

1. Importar o Metadados do banco correspondente (Oracle ou SQL) pela pasta `\Vidya\querys-vidya-force\...`.
2. Verificar se o pacote trouxe algum `.JAR` (ex.: `VIDYAUPDATESETTINGSCACHEEVENT.JAR`) e garantir que ele seja implantado corretamente junto ao Sankhya.
3. Criar, em seguida, o Lançador da mesma tela na pasta **Comercial**.
4. Repetir o processo tela a tela.
