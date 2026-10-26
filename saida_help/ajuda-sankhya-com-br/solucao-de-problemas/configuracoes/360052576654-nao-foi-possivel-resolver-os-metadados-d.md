---
id: "360052576654"
titulo: "Não foi possível resolver os metadados da entidade 'XXXXXXX'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360052576654-N%C3%A3o-foi-poss%C3%ADvel-resolver-os-metadados-da-entidade-XXXXXXX"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-09-23T11:32:47Z"
rotulos: ["Configuração", "Contrato", "Dicionário de Dados", "#formatadoroger", "CORE_E03945", "Erro de Metadados na Entidade Contrato", "Erro", "metadados", "Artigo atualizado KCS", "Financeiro - KCS", "Plataforma - KCS", "Banco de Dados"]
---

# Não foi possível resolver os metadados da entidade 'XXXXXXX'

**SITUAÇÃO**

Este erro pode ocorrer ao tentar acessar diferentes telas do sistema após atualização, replicação de base ou instabilidade.

**CAUSA**

Este erro ocorre devido a inconsistências nos metadados das tabelas do sistema, causadas por:

- **"Falhas no carregamento de metadados de add-ons"**: Comum após atualizações de addons como o **"IMPEX"**, onde entidades específicas não são sincronizadas automaticamente.
- **"Campos não inicializados ou customizados"**: O sistema não consegue processar corretamente campos que não foram declarados corretamente ou que foram removidos ou renomeados em atualizações.
- **"Campo ausente no banco"**: O campo existe no dicionário, mas não existe na estrutura física da tabela.
- **"Módulos desatualizados"**: Versões incompatíveis ou falhas na sincronização de metadados após atualizações de versão.
- **"Cache desatualizado"**: Cache de metadados que não foi recarregado após alterações no banco de dados.
- **"Sincronização"**: Falhas na sincronização entre o dicionário de dados e as estruturas do banco.

**POSSÍVEIS SOLUÇÕES**

**(1)** Alternativa 1:

- Acesse a tela **"Dicionário de Dados"** (Configurações >> Avançado >> Dicionário de Dados).
- Identifique na mensagem de erro a instância ou tabela relacionada. No campo de pesquisa, digite o nome da tabela ou o nome da instância.
- Selecione o registro na lista, clique nos **"três pontinhos"** e selecione a opção **"Reiniciar esta Unidade de Dados"**.
- Aguarde a conclusão do processo de reinicialização dos metadados.
- Caso o erro persista, siga para a próxima alternativa.

**(2)** Alternativa 2:

- Se na mensagem de erro apresenta o nome de um campo da tabela, verifique no "modo formulário" se o campo existe no "Dicionário de Dados".
- Abra a tela "DBExplorer", busque pela mesma tabela e verifique se o campo existe também.
- Se o campo existir no dicionário de dados, mas não no DBExplorer, será necessário criar o campo no banco de dados e depois reiniciar a unidade de dados (passos detalhados na alternativa 1).

**(3)** Alternativa 3:

- Se o erro passou a ocorrer, na base de teste, após replicar a base de produção na base de teste, provavelmente ocorre por um dos dois motivos a seguir:
  - A base de produção tem addons e a base de teste não tem os mesmos addons
  - A versão das bases está muito diferente
- Se for pela falta dos addons, basta instalar na base de teste para que os erros parem de ocorrer. Isso ocorre, pois a replicação da base copia todas as informações do banco de dados, inclusive dos addons, mas a instalação de addons não é feita automaticamente nesse processo.
  Se o addon já existe na base de teste, abra a tela "Minhas Soluções" e tente reiniciar o dicionário de dados do addon.
- Se for a versão muito diferente (geralmente a base de teste está atualizada para uma versão mais recente que a produção), pelo WPM, rode a mesma versão da base de teste novamente.

**(4)** Alternativa 4:

Se nenhum dos passos anteriores funcionar, tente limpar cache e reiniciar o sistema. E, caso, mesmo assim, o erro persistir, abra um chamado para seguir para análise técnica.
