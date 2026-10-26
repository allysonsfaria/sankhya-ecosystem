---
id: "40186439473047"
titulo: "Permissões de Acesso ao Gerenciador de Folhas"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40186439473047-Permiss%C3%B5es-de-Acesso-ao-Gerenciador-de-Folhas"
trilha: "Manual do Produto > Pessoas+ > Implantação e Acessos do Pessoas+ > Usuários e Permissões do Pessoas+"
atualizado_em: "2026-10-20T12:53:10Z"
rotulos: ["Configuração", "Segurança", "Painel de Configurações", "Gerenciador de Folhas", "Configuração de permissões", "Pessoal+", "Grupo de acessos", "Acesso para o Gerenciador de Folhas", "Permissões"]
---

# Permissões de Acesso ao Gerenciador de Folhas

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Configurações > Painel de Configurações
**ID da Tela:** br.com.sankhya.rh.ConfiguracoesDaFolha

---

### Descrição e Usabilidade

Para garantir a segurança e o controle das informações sensíveis da folha de pagamento, o sistema permite que você defina exatamente quais ações cada usuário (ou grupo de usuários) pode executar dentro do **Gerenciador de Folhas**.

Você deve configurar essas permissões sempre que um novo colaborador for atuar no departamento pessoal ou quando precisar ajustar as responsabilidades de um usuário existente, como promover alguém de uma função de apenas consulta para uma função de execução.

A configuração é feita através do **Painel de Configurações** e funciona em duas etapas: primeiro, você agrupa os usuários em **Grupos de Decisores**; depois, você atribui as permissões específicas do Gerenciador de Folhas a esse grupo. Isso permite que você gerencie as permissões de forma centralizada, em vez de ter que configurar usuário por usuário.

### Pré-requisitos

- Possuir acesso ao sistema com usuário ativo;
- Ter permissão de acesso às telas **Gerenciador de Folhas** e **Cálculos**;
- Estar vinculado a um **grupo de usuários** configurado no **Painel de Configurações**.

  Para saber como realizar essas liberações, acesse o artigo: [**Liberação de acesso às telas do módulo Pessoal+ para novos colaboradores**](https://ajuda.sankhya.com.br/hc/pt-br/articles/38583858942743).

### Jornada de Uso

O processo é simples e realizado dentro do Painel de Configurações.

[GIF animado: Imagem 1: O processo é simples e realizado dentro do Painel de Configurações.](https://ajuda.sankhya.com.br/hc/article_attachments/40278787025815)

1. Acesse a tela **Painel de Configurações** (Pessoal+ > Configurações);
2. Clique em **Configuração de permissões** e, em seguida, no card **Gerenciador de Folhas**;
3. Selecione o**Grupo de acessos** e os **usuários**;
4. Marque as ações que o usuário poderá executar:
   - **Análises**;
   - Gerar **Resumo da Folha**;
   - **Integrar com o Financeiro**;
   - **Integrar com a Contabilidade**;
   - **Excluir folhas**;
   - **Fechar / Reabrir folhas.**
5. Para dar todas as permissões, use a opção **Selecionar todas**;
6. Clique em **Confirmar alterações** para salvar a configuração.

   | **⚠️** **Atenção**  Não existe uma permissão específica para baixar ou enviar holerites. O botão **Download/Envio de Holerites e Relatórios de Médias** só aparece no **Gerenciador de Folhas** quando o grupo tem uma destas permissões marcadas:  - **Excluir folhas**; ou - **Apenas Consulta**. Se nenhuma das duas estiver marcada, o usuário não consegue baixar nem enviar holerites e relatórios de médias, mesmo com as demais permissões liberadas. |
   | --- |
7. A partir desse momento, o usuário vinculado terá o acesso as rotinas no **Gerenciador de Folhas**.

### Pontos de Atenção

- **Permissão Apenas Consulta:** esta é uma permissão especial e muito importante. Ao marcá-la, você poderá navegar por todas as abas do **Gerenciador de Folhas**, visualizar dados e consultar informações. Os botões de ação, como excluir, integrar e fechar, ficarão desabilitados. A exceção é o botão **Download/Envio de Holerites e Relatórios de Médias**, que continua disponível.
- **Permissões são por Grupo:** lembre-se que você está dando permissão a um grupo, não a um usuário individual. Se você adicionar um novo usuário a um grupo, ele automaticamente herdará todas as permissões daquele grupo.

### Dicas de Usabilidade

- **Segregação de Funções:** crie grupos diferentes para funções diferentes. Por exemplo, um grupo "Auditores" pode ter a permissão "Apenas Consulta", enquanto o grupo "Gestores de RH" tem permissão para integrar e fechar folhas.
- **Revise Periodicamente:** é uma boa prática revisar essas permissões de tempos em tempos, especialmente quando há mudanças na equipe, para garantir que o acesso de cada um continue adequado à sua função.

### Perguntas Frequentes (FAQ)

1. **Liberei a permissão para um usuário, mas ele disse que ainda não consegue executar a ação. O que pode ser?**

   Peça para o usuário sair e entrar novamente no sistema. As novas permissões geralmente são aplicadas após um novo login. Verifique também se você atribuiu a permissão ao grupo correto em que o usuário se encontra.
2. **Qual a diferença entre não marcar nenhuma permissão e marcar "Apenas Consulta"?**

   Nos dois casos, o usuário não executa ações operacionais, como excluir, integrar ou fechar folhas. A diferença está no download de holerites: com **Apenas Consulta**, o usuário consegue baixar e enviar holerites e relatórios de médias; sem nenhuma permissão marcada, o botão **Download/Envio de Holerites e Relatórios de Médias** não aparece.

   Além disso, usar a opção **Apenas Consulta** deixa registrada a intenção de que aquele grupo deve ter acesso apenas para visualização, o que facilita futuras manutenções.
3. **Posso dar permissões diferentes para usuários dentro do mesmo grupo?**

   Não. O sistema de permissões do Gerenciador de Folhas é baseado em grupos. Se você precisa de permissões diferentes, a solução é criar grupos diferentes (ex: "Analista Jr." e "Analista Pleno").
4. **Por que o usuário não vê a opção de baixar ou enviar holerites no Gerenciador de Folhas?**

   O botão **Download/Envio de Holerites e Relatórios de Médias** depende das permissões **Excluir folhas** ou **Apenas Consulta**. Se o grupo do usuário não tem nenhuma das duas marcadas, o botão não é exibido.

   Para liberar o download:

   - se o grupo pode excluir folhas, marque **Excluir folhas**;
   - se o grupo deve apenas consultar a folha e baixar holerites, marque **Apenas Consulta**. Nesse caso, as ações operacionais, como integrar e fechar folhas, ficam bloqueadas.

   Depois de alterar as permissões, peça para o usuário sair e entrar novamente no sistema.

### Artigos Relacionados

- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
- [Permissão para acesso de Apenas Consulta no Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40044327954071)
