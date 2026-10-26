---
id: "44010808234135"
titulo: "[TMS] - Painel de Aprovações"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010808234135--TMS-Painel-de-Aprova%C3%A7%C3%B5es"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:46:49Z"
rotulos: ["sync_hc", "lincros", "sync_hash_2f87b1cbba75", "lincros_13433311"]
---

# [TMS] - Painel de Aprovações

**Menu**: Operacional > Atividades > Painel de aprovações

**Objetivo:** O painel de aprovações permite visualizar as pendências e os status de cada rotina que utiliza alçada de aprovação. Essas rotinas podem ser: Cotação spot, Cotações contrato, Cargas, Faturas, Tabela de frete e Contrato de negociações. O Painel de aprovações segue o mesmo nível de hierarquia das alçadas.

**Considerações**:

- Estar habilitado os parâmetros usarAlcadaAprovacaoRespeitandoHierarquia e usarAlcadaAprovacao (correspondente a alçada de aprovação que deseja que seja exibida no painel de aprovações) como por exemplo usarAlcadaAprovacaoConhecimento;
- É necessário ter [alçada de aprovação](https://intercom.help/ajudalincros/pt-BR/articles/13439012-tms-como-configurar-a-alcada-de-aprovacao) cadastrada com o tipo de restrição correspondente (Ex: Faturas, Tabelas de frete, etc.);

## Como utilizar o Painel de Aprovações

**Exemplo**: Como utilizar o tipo de restrição Tabela de frete.

Ao acessar o Painel de Aprovações através do menu Operacional > Atividades > Painel de aprovação, com o usuário de primeiro nível, são apresentadas as tabelas que ainda não foram deferidas pelo usuário de nível 1 na árvore de alçada de aprovação;

![Imagem 1: Ao acessar o Painel de Aprovações através do menu Operacional > Atividades > Painel de aprovação, com o usuário de…](https://ajuda.sankhya.com.br/hc/article_attachments/44010778951063)

Para deferir, clique na ação:

![Imagem 2: Para deferir, clique na ação:](https://ajuda.sankhya.com.br/hc/article_attachments/44010797225239)

Para indeferir, clique na ação:

![Imagem 3: Para indeferir, clique na ação:](https://ajuda.sankhya.com.br/hc/article_attachments/44010772796055)

Ao clicar em '**Deferir**', o usuário de segundo nível recebe um e-mail solicitando a aprovação. Quando deferido pelo último aprovador, o processo é finalizado;

Ao clicar em '**Indeferir**', o registro é retornado para o usuário origem refazer.

Para que o sistema puxe registros mais antigos, o parâmetro 'diasParaBuscarObjetosParaAprovacao' deve ser ativado com período máximo recomendado de 120 dias. A tela de parâmetros somente o usuário 'Administrador' possui acesso de leitura, e os ajustes devem ser solicitados para o Suporte da Lincros.

**Obs.:** Quando uma alçada de aprovação de fatura for cadastrada somente com uma hierarquia de aprovação, ao ser importada uma fatura no sistema, a mesma não será demonstrada no painel de aprovação, visto que não há próximo aprovador para realizar o aceite.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
