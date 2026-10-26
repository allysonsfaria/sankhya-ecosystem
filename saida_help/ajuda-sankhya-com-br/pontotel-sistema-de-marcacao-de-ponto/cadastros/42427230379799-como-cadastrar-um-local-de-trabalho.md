---
id: "42427230379799"
titulo: "Como cadastrar um local de trabalho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427230379799-Como-cadastrar-um-local-de-trabalho"
trilha: "PONTOTEL: Sistema de marcação de ponto > Cadastros"
atualizado_em: "2026-08-03T13:29:55Z"
rotulos: ["sync_hc", "pontotel_6a332851b083ccbe02cce336", "sync_hash_5d4aad9a999d", "pontotel"]
---

# Como cadastrar um local de trabalho

Cadastrar corretamente os locais de trabalho na plataforma Pontotel facilita a gestão em diversos aspectos, como: alocação de feriados nas folhas, configurar uma [cerca virtual](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031) ou manter uma organização mais eficiente das folhas dos colaboradores.

Os locais de trabalho não precisam ser um espaço físico. Eles podem também representar equipes, departamentos ou setores, permitindo uma organização que melhor se ajuste às suas necessidades. Além disso, essa separação de locais de trabalho também serve como uma forma de limitar o acesso de gestores e supervisores às informações específicas de cada área, garantindo maior controle e privacidade na gestão. Use essa flexibilidade para estruturar os locais da forma mais conveniente para sua operação.

Neste artigo, você encontrará orientações sobre como preencher corretamente cada campo no cadastro de um local de trabalho.

---

## Como cadastrar um local de trabalho:

1. No menu de navegação do[site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros** e, em seguida, selecione **Locais de trabalho**.
2. Clique em **Criar novo local de trabalho**.
3. Preencha os campos necessários:

![Imagem 1: Preencha os campos necessários:](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1qq1nn7.png)

- **Nome do local de trabalho**: Dê um nome que identifique o local de trabalho.
- **Código**: Use esse campo para inserir um identificador único para o local. Ele ajuda a organizar e diferenciar facilmente os cadastros, facilitando a consulta e o gerenciamento no dia a dia. Pode ser o mesmo usado na folha de pagamento, ou o centro de custo do departamento/setor.
- **Região (País, Estado e Município)**: Defina aqui a região do local de trabalho. Primeiro, selecione o país; em seguida, a opção para escolher o estado (UF) será habilitada, e por fim, escolha o município. Preencher esses campos corretamente é essencial, pois a localização do local de trabalho é usada para alocar automaticamente os feriados nas folhas de ponto dos colaboradores.
- **Fuso horário**: Utilize este campo para definir o fuso horário do local de trabalho. Essa configuração é importante para garantir que os registros de ponto sejam registrados corretamente, de acordo com o horário local da região. 💡**Dica**: O padrão GMT -03:00 corresponde à opção "America/Sao\_Paulo", que é o horário oficial de Brasília e utilizado na maior parte do Brasil. Se o local de trabalho estiver em uma região com horário diferente, selecione o fuso horário correspondente.
- **Empregadores:** Selecione um ou mais empregadores que estejam vinculados a esse local. É importante garantir que o empregador selecionado no cadastro do empregado também esteja selecionado no local de trabalho do colaborador, permitindo uma associação correta entre o empregado, empregador e local de trabalho.
- **Sincronizar com REP-P**: É obrigatório selecionar essa opção para garantir que as configurações do local de trabalho sejam sincronizadas com todos os dispositivos. Caso contrário, os colaboradores desse local de trabalho não conseguirão registrar o ponto nos dispositivos utilizados para registrar o ponto (coletores).
- **Descrição do local no AFD e comprovante de ponto**: Este campo deve conter o nome do local que aparecerá nos arquivos mencionados, facilitando a identificação. Por padrão, você pode repetir o nome do local de trabalho.
- **Ativar local de trabalho**: Mantenha ativado para que o local possa ser utilizado no sistema.
- **Escolher no mapa a localização do local de trabalho**: Ative para definir o endereço do local.
- **Digite um local**: Caso a opção acima tenha sido ativada, este campo aparecerá. Digite um CEP ou endereço. Enquanto digita, é possível selecionar o endereço na lista que aparecerá logo abaixo. Ao selecionar o endereço, novos campos aparecerão preenchidos. Complete o preenchimento com o número e complemento (caso haja) do local. Se o marcador no mapa não estiver exatamente no local correto, basta arrastá-lo para ajustar a localização com precisão.
- **Distância máxima da cerca virtual**: Preencha para definir uma distância máxima (em metros) para [cerca virtual](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031) no local, com prioridade sobre o valor definido atualmente no [perfil de coletor](https://sankhya.zendesk.com/hc/pt-br/articles/42427310963095).

> 💡 **Dica**: Definir o endereço do local é essencial caso você queira [configurar uma cerca virtual](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031) para restringir o registro de ponto no local de trabalho, pois o endereço definido será utilizado como referência para validar os registros de ponto.

**Configurações avançadas**
Por padrão, pode deixar esses campos em branco, mas há opções que permitem ajustes mais específicos para os locais de trabalho.

- **Mostrar local de trabalho noa acompanhamento de entrada**: Ative para que o local fique visível nos dashboards de acompanhamento do sistema.
- **Prioridade**: Defina a importância desse local, ordenando sua posição para facilitar a visualização nos dashboards de acompanhamento do sistema.
- **Regras de cálculo específico para local de trabalho:** Vincule uma regra ao local caso haja uma configuração de cálculo para uma necessidade específica do local. Se não for selecionada nenhuma regra, os cálculos serão feitos com base na regra de cálculo vinculada ao cadastro do empregado.
- **Aceitar timezone do coletor:** Ative esta opção se preferir que os registros de ponto dos colaboradores sejam registrados de acordo com o fuso horário do dispositivo utilizado para a marcação, ao invés do fuso horário do local de trabalho. Essa opção é utilizada caso o coletor tenha um fuso horário diferente do local de trabalho.
- **Telefone**: Inclua os números de telefone disponíveis no local de trabalho para manter no cadastro.
- **Adicionar novo campo customizado:** Clique nessa opção para criar novos campos personalizados na jornada. Essa funcionalidade é útil para empresas que precisam registrar informações extras que não fazem parte dos campos padrões da plataforma.

4. Depois de preencher os campos , clique em **Salvar**.

---

> 💡 Dica: A Pontotel conta com o Tour Guiado, uma funcionalidade interativa disponível dentro do próprio site Pontotel Gestão, criada para auxiliar você na configuração de cadastros, parametrizações e utilização das principais ferramentas da plataforma. Com orientações passo a passo diretamente na tela, o Tour ajuda a tornar o processo mais simples, rápido e intuitivo, reduzindo dúvidas e evitando erros durante as configurações. Sempre que precisar, você poderá ativar a funcionalidade em: Admin > Tour. Para mais detalhes sobre como utilizar o recurso, confira o artigo: [Como utilizar o Tour Guiado](https://sankhya.zendesk.com/hc/pt-br/articles/42427249823127).

---

Pronto! Seu novo local de trabalho foi configurado com sucesso e já está disponível na plataforma. Com essas definições ajustadas, você garantirá maior precisão no acompanhamento das jornadas e na gestão das folhas de ponto, tornando sua operação mais eficiente e organizada!

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
