---
id: "17268960280727"
titulo: "Como gerar o resumo da folha"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/17268960280727-Como-gerar-o-resumo-da-folha"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Conferência e Auditoria da Folha"
atualizado_em: "2026-10-02T15:39:52Z"
rotulos: ["Configuração", "Relatórios", "Impostos", "FPREGFISCAL", "Resumo da folha", "Folha de Pagamento", "FPNOVORESUMOFOL", "Gerenciador de folhas", "FPRELRESFOLHA", "Filtrar e selecionar folhas", "Pessoal+", "FPCOMPENSCAMPO9", "ZERARESC", "Documentos Eletrônicos"]
---

# Como gerar o resumo da folha

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Gerenciador de Folhas > Resumo da Folha
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

---

## Descrição e Usabilidade

### 1. Descrição da Funcionalidade

O **Resumo da Folha** gera um relatório analítico da folha calculada, permitindo conferir valores, contribuições e totais por funcionário de forma rápida e segura.

### 2. Pré-requisitos

Antes de gerar o resumo, verifique:

**(3)Acesso à(s) empresa(s)**

- Usuário inserido no **Grupo de decisores** (Painel de Configurações ) correspondentes à(s) empresa(s).

  - Acesse o **Painel de Configurações**(Pessoal+ > Configurações > Painel de Configurações).
  - Vá até a seção **Grupo de Decisores**.
  - Clique sobre o card do **grupo de usuários**, em seguida, certifique-se de que a empresa esteja na lista ao lado direito da tela.

    Caso não esteja, basta clicar no sinal de **adição** e adicionar a empresa desejada.

  [GIF animado: Imagem 1: Caso não esteja, basta clicar no sinal de adição e adicionar a empresa desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/39732942951703)

**(3)Permissão concedida para gerar o resumo da folha**

- Acesse o **Painel de Configurações**(Pessoal+ > Configurações > Painel de Configurações).
- Vá até a seção **Configuração de Permissões**.
- Selecione a tela **Gerenciador de Folhas**, em seguida, o grupo de usuários desejado e certifique-se de que a permissão **Resumo da Folha** esteja habilitada.

  [GIF animado: Imagem 2: Selecione a tela Gerenciador de Folhas , em seguida, o grupo de usuários desejado e certifique-se de que a permissão…](https://ajuda.sankhya.com.br/hc/article_attachments/39733137591063)

(3)**Folha calculada**

- A folha deve estar **calculada** na referência desejada.

(3)**Registro Fiscal por Departamento (quando aplicável)**

- Se a empresa utiliza Registro Fiscal por Departamentos (parâmetro **FPREGFISCAL**), é obrigatório preencher o campo **Registro Fiscal** na aba **Geral** do cadastro de **todos os Departamentos**.

  Vale lembrar que o **departamento** é usado apenas para casos de tomadores de serviço.

(3)**Configuração das bases de cálculo**

- Base IRRF → Evento **1904** com Identificação da base = **12**
- Base INSS → Evento **1901** com Identificação da base = **8**

### 3. Jornada de Uso

1. Acesse o **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha).

2. Filtre:

- Empresa;
- Referência;
- Tipo da folha;
- Status.

![Imagem 3: Status.](https://ajuda.sankhya.com.br/hc/article_attachments/17268683476759)

3. Localize a folha calculada e clique sobre ela.

4. Clique no botão **Resumo da Folha** (ícone da impressora).

![Imagem 4: 4. Clique no botão Resumo da Folha (ícone da impressora).](https://ajuda.sankhya.com.br/hc/article_attachments/17268661235607)

5. Configure o pop-up nas abas:

- Empresas;
- Geração;
- Departamentos;
- Ordenação Funcionários;
- Funcionários.

![Imagem 5: Funcionários.](https://ajuda.sankhya.com.br/hc/article_attachments/17268714344087)

Configure cada aba conforme a sua necessidade.

![Imagem 6: Configure cada aba conforme a sua necessidade.](https://ajuda.sankhya.com.br/hc/article_attachments/17268706062359)

6. Clique em:

- **Download PDF** ou
- **Pré-visualizar**

![Imagem 7: Pré-visualizar](https://ajuda.sankhya.com.br/hc/article_attachments/35934417899031)

7. Confira os valores de Fundo de Garantia do Tempo de Serviço (FGTS) no corpo e no rodapé do resumo.

O Resumo da Folha apresenta o FGTS em dois pontos, com formas de cálculo diferentes:

- **Corpo do relatório**: o sistema apresenta o evento **995 – FGTS NORMAL** de cada colaborador. O valor é calculado individualmente: o sistema aplica o percentual de FGTS sobre a base de FGTS do colaborador e **trunca** o resultado em duas casas decimais, ou seja, descarta as casas excedentes sem arredondar. Os totais do evento 995 no corpo são a soma desses valores individuais já truncados.
- **Rodapé do relatório**: na seção **Total Guia** (ou **Total Geral Guia**, no total geral), o quadro **Dados FGTS** soma primeiro as bases de FGTS de todos os colaboradores e depois aplica o percentual sobre essa base total. O truncamento em duas casas decimais acontece uma única vez, sobre o valor total. O quadro separa as linhas **Remuneração s/13 Sal**, **Remuneração c/13 Sal** e **Remun. s/13 Rescisão**, agrupadas por percentual, e fecha com a linha **Total**.

Como o truncamento individual descarta frações de centavo de cada colaborador, a soma do evento 995 no corpo pode ficar alguns centavos **abaixo** do valor apresentado em **Dados FGTS** no rodapé. Quanto maior o número de colaboradores, maior tende a ser a diferença. Esse comportamento é esperado e não indica erro no cálculo da Folha de Pagamento.

**Exemplo** (percentual de FGTS de 8%):

| Colaborador | Base de FGTS | Cálculo sem truncar | Evento 995 (truncado) |
| --- | --- | --- | --- |
| Colaborador A | R$ 1.234,56 | R$ 98,7648 | R$ 98,76 |
| Colaborador B | R$ 2.345,67 | R$ 187,6536 | R$ 187,65 |
| Colaborador C | R$ 3.456,78 | R$ 276,5424 | R$ 276,54 |
| **Total** | **R$ 7.037,01** | — | **R$ 562,95** |

No rodapé, o sistema calcula 8% sobre a base total de R$ 7.037,01, o que resulta em R$ 562,9608, truncado para **R$ 562,96**. A diferença de R$ 0,01 em relação ao corpo vem apenas do momento em que o truncamento é aplicado.

| **⚠️** **Atenção**  Para conferir o FGTS a recolher, não use a soma do evento 995 do corpo do Resumo da Folha. Use o evento S-5003 – Informações do FGTS por Trabalhador, que é o retorno do eSocial com o FGTS apurado. O valor do S-5003 fica alinhado ao total de **Dados FGTS** no rodapé, e não à soma do evento 995 no corpo.  No dashboard **S-5003 - Conferência de Informações do FGTS por Trabalhador**, a coluna **Depósito Mensal (Sistema)** também é formada pelo evento 995 de cada colaborador. A soma dessa coluna segue, portanto, a mesma lógica do corpo do Resumo da Folha. O valor apurado pelo eSocial aparece na coluna **Depósito Mensal (eSocial)**.  📚 Para saber mais, acesse [**S-5003 - Informações do FGTS por Trabalhador**](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591). |
| --- |

### 4. Pontos de Atenção

#### ✅ Parâmetros importantes

- **FPRELRESFOLHA**: define o código do modelo do relatório cadastrado na tela **Relatórios Formatados**.
- **FPCOMPENSCAMPO9**: ativa a compensação dos valores referentes à **retenção de terceiros**.

  Quando habilitado, o sistema deduz automaticamente o valor retido nas notas das contribuições previdenciárias devidas no mês, incluindo valores de outras entidades e fundos. Isso permite compensar esses valores diretamente na competência.
- **ZERARESC**: apresenta o valor líquido das rescisões que estiverem zeradas.
- **ZERARFER**: apresenta o valor líquido das folhas de férias que estiverem zeradas.

  Acesse o artigo [Zeramento de Férias e Rescisão no Resumo da Folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/4544050476951) para melhor compreensão.

#### ✅ Valor Parte Empresa

Certifique-se de que a opção **INSS Emp. Func:** esteja marcada na aba **Geral** do **Registro Fiscal** vinculado à empresa, bem como os percentuais dos tributos e encargos aplicáveis à empresa que irão compor os cálculos e guias.

#### ✅ Exibição do CNPJ da Filial no Relatório

Para visualizar o **CNPJ da Filial** no relatório, a opção **Imprimir apenas totalizadores** não deve estar habilitada.

Quando essa opção estiver desmarcada, o relatório apresentará:

- no primeiro cabeçalho, as informações da **Matriz**;
- logo abaixo da **Competência**, os dados da **Filial**, incluindo o respectivo CNPJ.

Caso a opção esteja marcada, o sistema exibirá apenas os totalizadores, sem detalhar as informações por estabelecimento.

#### ✅ Contribuições Previdenciárias (INSS sobre a Receita Bruta)

As **Contribuições Previdenciárias (INSS sobre a Receita Bruta)** somente serão apresentadas quando houver **valor maior que zero** informado no campo **“Valor do INSS da Receita Bruta”**, localizado na aba **Desoneração da Folha** do **Registro Fiscal**.

#### ✅ Retenção de terceiros

Para que os valores referentes à **retenção de terceiros** sejam gerados **tanto na guia GPS quanto no Resumo da Folha**, é necessário garantir as seguintes configurações:

- **Parâmetro FPCOMPENSCAMPO9 ligado**: esse parâmetro habilita a compensação dos valores de retenção de terceiros nas contribuições previdenciárias.
- **Na geração da guia GPS**, a opção **Utiliza valor de retenção no 13º salário** deve estar desmarcada.
  As retenções não se aplicam às folhas de 13º salário, portanto essa opção não deve ser marcada.
- **Na geração do Resumo da Folha, os tipos de folha selecionados devem ser os mesmos utilizados na geração da GPS**, **exceto o tipo 13º Salário**, que **não deve ser incluído**, pois não participa dessa dedução.

#### ✅ PIS sobre a folha

1. Configurar na tela **Registro Fiscal**, aba **Geral**, que a **Empresa** é **Contribuinte**, informar o **Código de Receita** e o valor da **Alíquota**.
2. Criar eventos com Bases de Cálculo configuradas:
   - Evento Base PIS = 20
   - Evento PIS = 114
   - Desmarcar a opção Imprime em documentos para esses dois eventos.
   - Vincular a [base de cálculo do PIS](https://ajuda.sankhya.com.br/hc/pt-br/articles/28240000315543-PIS-sobre-a-folha-de-pagamento#Basedec%C3%A1lculo) a todos os eventos que dependem dela.
3. Cálculos confirmados
   - Folha Mensal deve ter todos os eventos do item acima calculados individual ou coletivamente.

#### ✅ Licença-maternidade – Conferência de INSS e Compensação

Os valores pagos a título de licença-maternidade **não possuem incidência de INSS patronal** e podem ser utilizados para **compensação**.

Se houver divergência nos valores apurados, realize as seguintes verificações:

1. **Configuração dos eventos de licença-maternidade**

   Verifique se os eventos de licença gestante estão configurados com a **identificação** correta.

   Essa identificação é indispensável para que o **Resumo da Folha**, a **Guia GPS** e a **Integração com o Financeiro** realizem o cálculo correto da compensação e da apuração previdenciária.
2. **Parâmetros na emissão do Resumo da Folha**

   Ao gerar o relatório, na aba **Resumos**, marque as opções:

   ✔ **Demonstrar Resumos de Previdência e FGTS**

   ✔ **Utiliza Valores de Retenção/Compensação de INSS**

   Essas opções são fundamentais para empresas que possuem valores de licença-maternidade a compensar, garantindo que o relatório apresente corretamente os valores previdenciários.

#### ✅ Rescisões

Caso haja divergência entre o valor da multa do FGTS apresentado no resumo da rescisão e o valor exibido no FGTS Digital, verifique o evento utilizado no cálculo e a fórmula configurada para a multa.

### 5. Dicas de Usabilidade

- Utilize os mesmos tipos de folha do processo de geração da GPS para manter a consistência das conferências.
- Gere o resumo agrupado por Matriz/Filial para conferência com o eCAC.
- Use o resumo por departamento apenas para análises internas detalhadas.
- Revise as bases de cálculo dos eventos sempre que houver divergência de valores.

## Artigos Relacionados

- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424800696599)
- [Cadastro de Eventos e Bases de Cálculo](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Relatório S-5003 – Conferência de Informações do FGTS por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/36626761293591)
