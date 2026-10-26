---
id: "360045116353"
titulo: "Plano de Contas Referencial"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360045116353-Plano-de-Contas-Referencial"
trilha: "Manual do Produto > Fiscal e Contábil > Contábil > Contabilidade"
atualizado_em: "2026-07-29T16:02:14Z"
rotulos: ["AJUDA DO SKW", "manual", "Configuração", "ECF", "Contas", "Plano", "Referencial", "br.com.sankhya.contab.planodecontasreferencial", "Plano de Contas Referencial manual", "Importação", "Contabilidade", "Plano de Contas", "Importação de Planos de Contas Referenciais"]
---

# Plano de Contas Referencial

```
![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/42314991343767) Módulo: Contabilidade > Conexão > ECF > Configuração P/ ECF
```

---

Por meio desta tela é realizada a importação dos Planos de Conta salvos pelo PVA do ECF para o sistema, visando facilitar a atualização das informações pertinentes ao [Plano de Contas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360025234874-Plano-de-Contas) da Empresa.

![Imagem 2: Por meio desta tela é realizada a importação dos Planos de Conta salvos pelo PVA do ECF para o sistema, visando…](https://ajuda.sankhya.com.br/hc/article_attachments/33532280538519)

Para o uso da tela, primeiramente defina o **"Tipo"** de Plano de Contas a ser trabalhado; assim, temos as seguintes opções:

- 1 - PJ em Geral (L100\_A + L300\_A);
- 2 - PJ em Geral - Lucro Presumido ( P100 + P150 );
- 3 - Financeiras ( L100\_B + L300\_B );
- 4 - Seguradoras ou Entidades Abertas de Previdência Complementar ( L100\_C + L300\_C );
- 5 - Imunes e Isentas em Geral ( U100\_A + U150\_A );
- 6 - Financeiras - Imunes e Isentas ( U100\_B + U150\_B );
- 7 - Seguradoras - Imunes e Isentas ( U100\_C + U150\_C );
- 8 - Entidades Fechadas de Previdência Complementar ( U100\_D + U150\_D );
- 9 - Partidos Políticos ( U100\_E + U150\_E );
- 10 - Financeiras - Lucro Presumido ( P100B + P150B ).

Uma vez definido o Tipo de Plano de Contas, o sistema automaticamente filtra e carrega na grade predominante da tela, os Planos de Conta Referenciais correspondentes.

O botão **"Importar Plano ECF 2025"** permite que o usuário importe o plano de contas referencial exigido pelo ECF 2025, utilizando um arquivo no formato .xlsx conforme padrão oficial disponibilizado pelo governo. Ao clicar no botão, é aberto um pop-up para seleção do arquivo. O sistema processa todas as abas presentes no .xlsx e grava as informações do plano de contas referencial nas tabelas correspondentes, permitindo que as contas importadas tenham o mesmo comportamento das importações anteriores. Esta opção é exclusiva para a rotina de importação do plano de contas ECF 2025, sem interferência nas demais funcionalidades da tela.

Ao clicar no botão **"Atualizações Sped ECF"**, o sistema verifica se existe algum arquivo pertinente às Tabelas Dinâmicas para ser importado e/ou atualizado; caso afirmativo, tem-se a importação/atualização das Tabelas Dinâmicas do ECF correspondentes ao Tipo de Plano de Contas inicialmente definido.

**Observação:** a verificação da necessidade e a consequente importação/atualização das Tabelas Dinâmicas, é feita através da aplicação [Sankhya Web Connection](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596394) e Jiva Web Connection, que irá executar localmente na máquina de cada usuário. Assim, observe o caminho da Importação/Atualização:

1.Uma atualização das Tabelas Dinâmicas através do aplicativo da Receita, o Sped ECF. Este aplicativo pode ser obtido através do link [SPED ECF](http://idg.receita.fazenda.gov.br/orientacao/tributaria/declaracoes-e-demonstrativos/sped-sistema-publico-de-escrituracao-digital/escrituracao-contabil-fiscal-ecf/programa-sped-contabil-fiscal-para-windows);

2.O Sankhya Web Connection/Jiva Web Connection irá compactar esses arquivos e enviar para o Repositório de Arquivos (servidor) do Sankhya Om/Jiva Evo;

3.O Sankhya Om/Jiva Evo irá descompactar o arquivo que está no Repositório de Arquivos e proceder com a atualização das tabelas dinâmicas.
