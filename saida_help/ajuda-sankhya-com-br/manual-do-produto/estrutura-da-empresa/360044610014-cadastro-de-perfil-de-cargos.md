---
id: "360044610014"
titulo: "Cadastro de Perfil de Cargos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044610014-Cadastro-de-Perfil-de-Cargos"
trilha: "Manual do Produto > Pessoas+ > Configurações e Cadastros > Estrutura da Empresa"
atualizado_em: "2026-09-27T14:16:12Z"
rotulos: ["manual", "Perfil", "Perfil manual", "Configuração", "Requisitos", "QTDMAXREGEXPORT", "Folha", "Cargos", "Competências", "Descrição Analítica dos Cargos", "Exame Médico", "Exposição a Riscos", "Habilidades", "Histórico de Ocorrência", "Qualificações", "RH/Folha", "Treinamentos", "br.com.sankhya.pes.cad.perfil", "Cadastro", "Configuração Hierárquica de Perfis no Sistema RH/Folha", "Pessoal+", "RH"]
---

# Cadastro de Perfil de Cargos

```
 Módulo: Pessoal+ > Cadastros
```

---

![Imagem 1](https://ajuda.sankhya.com.br/hc/article_attachments/360096097193)

A tabela de **"Perfil"** possui estrutura hierárquica e por isto é possível definir o cadastro de cada **"Família de Perfis"**. A estrutura hierárquica deste cadastro pode ser definida no parâmetro **"Mascara para Perfil da Folha / RH - FPMASCPERFIL"**.

Os Perfis (RH/Folha) são criados para, posteriormente, serem informados nos **"Cargos"**, permitindo assim montar a **"Descrição Analítica destes Cargos"**.

Nesta tela, é possível criar hierarquias para, por exemplo, **"Treinamentos"**, **"Competências"**, **"Habilidades"**, **"Requisitos"**, **"Qualificações"**, **"Áreas de Resultado"** (para avaliações de Desempenho), **"Exames Médicos"**, **"Equipamentos de Proteção Individual"**, **"Exposição a Riscos"** etc.

Toda e qualquer informação, onde deseja-se que ela esteja presente nos **"Cargos"**, podem ser criadas anteriormente nos **"Perfis"**.

Para um novo cadastro, clique sobre o botão de inserção de um novo registro ![Imagem 2: Para um novo cadastro, clique sobre o botão de inserção de um novo registro , onde você informa um novo "Código" e sua…](https://ajuda.sankhya.com.br/hc/article_attachments/16695381178903), onde você informa um novo **"Código"** e sua correspondente **"Descrição"** para o perfil.

Se a marcação **"Ativo"** estiver desabilitada, mesmo após a criação do perfil este não poderá ser visualizado nos demais cadastros do sistema. Para que o perfil esteja disponível em outras rotinas, esta marcação deve estar selecionada.

A marcação **"Analítico"**, quando efetuada, representa que o cadastro não possuirá registros **"filhos"**; ao deixá-lo desmarcada, teremos um registro sintético, que poderá receber outros cadastros subsequentes.

**Nota:** as opções Ativo e Analítico serão apresentadas automaticamente marcadas pelo sistema na inclusão de um novo perfil. Nas demais rotinas do sistema, apenas serão aceitos os perfis Analíticos.

A marcação **"Requisito"**, quando efetuada, terá a representação de um perfil que a empresa considera requisito para preenchimento de uma determinada vaga. O perfil que possuir esta marcação assinalada, será apresentado para escolha na tela [Currículos](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045119493-Curr%C3%ADculos), aba **"Perfil Requisitos"**.

A marcação **"Exame"** deverá ser efetuada quando se tratar de um perfil para **"Exames Médicos"**.

Através da marcação **"Nível Hierárquico"**, você define que o perfil que está sendo cadastrado servirá para escolha de Níveis Hierárquicos em outras telas no sistema.

De forma semelhante à marcação anterior, a marcação **"Área Profissional"**, quando efetuada, determinará que o perfil em questão poderá ser definido como Áreas Profissionais em outras rotinas no sistema.

**Observação:** as duas marcações citadas por último, quando realizada, fará com que seus perfis correspondentes sejam apresentados para escolha nas abas **"Perfil Nível Hierárquico"** e **"Perfil Área Profissional"** na tela Currículos.

O campo **"Cód. Histórico de Ocorrência"** somente será habilitado quando a marcação Exame estiver realizada, e servirá para que sejam informados Históricos de Ocorrências padrão para cada Exame cadastrado nos Perfis.

O campo **"Observação"** pode ser utilizado para a inserção de informações relevantes em relação aos perfis cadastrados.

Na barra de ferramentas temos os seguintes botões:

![Imagem 3: Através deste botão você realiza a "Configuração da Grade" , onde é possível configurar quais colunas estarão visíveis,…](https://ajuda.sankhya.com.br/hc/article_attachments/16695473503767) Através deste botão você realiza a **"Configuração da Grade"**, onde é possível configurar quais colunas estarão visíveis, além de visualizar a árvore em modo grade ou formulário.

![Imagem 4: O botão "Impressão do Grid" possibilitará a impressão dos registros da grade em formato "PDF" , "XLS" e sua…](https://ajuda.sankhya.com.br/hc/article_attachments/16695487030039) O botão **"Impressão do Grid"** possibilitará a impressão dos registros da grade em formato **"PDF"**, **"XLS"** e sua visualização em cubo.

**Nota:** por meio da configuração do parâmetro **"Qtd. máx. de reg. para export. de PDF, XLS e Cubo - QTDMAXREGEXPORT"**, temos a possibilidade de limitar a quantidade máxima de registros que serão exportados na utilização das funcionalidades **"Exportar como PDF"**, **"Exportar como planilha"** e **"Visualizar em cubo"**. Informe um número inteiro, que represente o limite de registro que serão exportados, por exemplo 50 registros, 100 registros; dependendo da sua necessidade.

![Imagem 5: Esta tela dispõe também do botão para a criação de filtros personalizados. Contudo, os filtros aqui configurados,…](https://ajuda.sankhya.com.br/hc/article_attachments/16695536593175) Esta tela dispõe também do botão para a criação de filtros personalizados. Contudo, os filtros aqui configurados, somente serão aplicados nos registros filhos.

**Importante:** independente do critério de filtro criado, o sistema adicionará um critério com a condição **AND (Perfil.ANALITICO = N)**. Dessa forma, o sistema filtrará os registros que satisfaçam o filtro criado, e também filtrará todos os registros que não são analíticos.
