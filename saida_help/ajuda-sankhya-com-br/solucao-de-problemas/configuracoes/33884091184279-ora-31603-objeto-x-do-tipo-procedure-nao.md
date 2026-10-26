---
id: "33884091184279"
titulo: "ORA-31603: objeto 'X' do tipo procedure não encontrado no esquema 'Y'"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33884091184279-ORA-31603-objeto-X-do-tipo-procedure-n%C3%A3o-encontrado-no-esquema-Y"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T14:28:05Z"
rotulos: ["SQL", "Configuração", "sankhyaflow", "Razão do erro", "Detalhe do erro", "banco de dados", "Erro", "Flow", "NO_DO_OBJETO", "não encontrado no esquema 'Y'", "ORA-31603", "procedure", "objeto 'X' do tipo procedure"]
---

# ORA-31603: objeto 'X' do tipo procedure não encontrado no esquema 'Y'

**MENSAGEM:**

ORA-31603: objeto 'X' do tipo procedure não encontrado no esquema 'Y'

**SITUAÇÃO:**

Ao exportar um processo de negócio na rotina Flow, a mensagem de erro é apresentada.

**Atenção:** Para avançar com a correção, é necessário conhecimento técnico em **banco de dados**, pois a investigação e a resolução envolvem consultas SQL e a identificação de elementos estruturais do sistema.

**SOLUÇÃO:**

Ao exportar um processo no Flow, o sistema automaticamente inicia a exportação dos metadados das instâncias envolvidas, incluindo botões de ação, eventos personalizados, triggers e outros elementos vinculados ao processo.

Assim, se algum botão de ação estiver associado a um objeto (como uma procedure) que não existe mais no banco de dados, um erro será gerado.

Para identificar onde esse objeto está sendo referenciado, execute a consulta SQL abaixo, substituindo **''NO\_DO\_OBJETO''** pelo nome exato do objeto mencionado na mensagem de erro:

```
SELECT * FROM TSIBTA WHERE CONFIG LIKE '%NO_DO_OBJETO%'
```

**(1)** A consulta retornará os registros onde o objeto está sendo citado. Assim, será possível identificar **qual instância o botão de ação** está com essa referência obsoleta;

**(2)** Após localizar o componente, acesse a tela correspondente no sistema a instância, podendo ser o ''**Dicionário de Dados'', ''Construtor de Telas''** ou ''**Formulários Formatados'';**

**(3)** Localize a tabela identificada, vá até a **aba Ações**, e verifique qual botão de ação está referenciando o objeto ausente citado na mensagem de erro;

**(4)** Após isso, será necessário realizar uma análise:

- Se o objeto (procedure) foi excluído propositalmente, é recomendável remover o botão de ação;
- Se o objeto foi removido por engano, é possível recriá-lo no banco (desde que a lógica da procedure esteja disponível e seja válida).

**CAUSA:**

O erro ocorre porque botões de ação no Flow ainda referenciam objetos removidos do banco de dados.

Durante a exportação, o sistema busca todos os componentes associados, incluindo procedures citadas nos botões. Se o objeto não for encontrado, é gerado o erro **ORA-31603**.

Esse problema geralmente surge após manutenções no banco, como exclusão de procedures obsoletas, sem atualização das configurações, comprometendo a consistência da exportação.
