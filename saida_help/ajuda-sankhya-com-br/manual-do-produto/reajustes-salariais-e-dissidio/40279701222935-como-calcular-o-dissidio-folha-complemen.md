---
id: "40279701222935"
titulo: "Como calcular o dissídio (folha complementar)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Reajustes Salariais e Dissídio"
atualizado_em: "2026-10-02T15:38:13Z"
rotulos: ["Configuração", "Eventos", "Impostos", "ID: br.com.sankhya.rh.ReajusteSalarial", "br.com.sankhya.rh.RegrasCalculo", "Folha de Pagamento", "Dissídio", "ID: br.com.sankhya.rh.Sindicato", "Reajuste Salarial", "Pessoal+", "ID: br.com.sankhya.rh.CadastroEventos", "Reajuste Salarial CCT", "Cálculo de Dissídio (Folha Complementar)", "FPCALCDISSMEM"]
---

# Como calcular o dissídio (folha complementar)

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Cálculos
**ID da Tela:** br.com.sankhya.rh.CalculoIndFolha

---

### Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8KA8C1WHDYD8VMSXWQSJP)
[Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8F3F9ZZG632CJX7EK4WTP)
[Jornada de Uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8F3FTBV85YFCESYS0R2W2)
[Pontos de Atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8J35H65PH2Z75PDP4XRRK)
[Perguntas Frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8F3GR04P6C67XWZ7YVYE0)
[Artigos Relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/40279701222935-Como-calcular-o-diss%C3%ADdio-folha-complementar#h_01KQZ8F3H0X7XEDXRBAJ9Y7AVQ)

---

### Descrição e Usabilidade

O cálculo de dissídio (folha complementar) é utilizado para apurar e pagar **diferenças salariais retroativas**, normalmente originadas por:

- Convenção Coletiva (CCT);
- Acordo coletivo;
- Reajustes aplicados após a data-base.

Essas diferenças são calculadas com base no novo salário e comparadas com os valores já pagos, gerando uma folha complementar.

### Pré-requisitos

Antes de calcular o dissídio, é essencial validar as configurações abaixo:

**(1)** **Cadastro de Eventos**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.CadastroEventos

1. Acesse a tela [**Eventos**](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911) (Pessoal+ > Cadastros) e confira se todos os eventos que deverão participar do cálculo de dissídio estão:

   - ativos;
   - com o checkbox **Tem seus valores recalculados** marcado na aba **Avançado**;
   - em casos de recálculo de rescisão, onde serão pagas as diferenças de verbas indenizadas, observar também se o checkbox **Evento de indenização integrante do Aviso Prévio Indenizado** está marcado;
   - verifique se as bases de cálculo dos impostos (INSS, IRRF, FGTS) estão com a opção **Complementar** no campo **Evento como regra em cálculo de** na aba **Básico**.

     | **⚠️** **Atenção**  Isso permite que o sistema trate corretamente os valores retroativos. |
     | --- |

**(2)**  **Regras de Cálculo**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.RegrasCalculo

1. Entre na tela [**Regras de Cálculo**](https://ajuda.sankhya.com.br/hc/pt-br/articles/39936375428503) (Pessoal+ > Cadastros), aba **Propriedades** > Geral > Reajuste Sindical e  configure conforme o tipo de colaborador:

- **Mensalistas**: marque **Aplicar percentual em todos os eventos da folha complementar (mensalistas)**;
- **Horistas/Diaristas**: marque **Aplicar percentual em todos os eventos da folha complementar (não mensalistas)**.

  Essa configuração garante que o percentual de reajuste seja aplicado corretamente nos eventos.
- **Admissões durante o período de referência**: marque **Considerar mês de admissão independente dos dias trabalhados** para que o sistema inclua corretamente o mês de admissão no cálculo do dissídio, mesmo quando o colaborador não trabalhou o mês completo. Sem essa marcação, colaboradores admitidos durante o período da convenção podem apresentar inconsistências no cálculo.

**(3)** **Cadastro do Sindicato (CCT)**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Cadastros
**ID da Tela:** br.com.sankhya.rh.Sindicato

1. Acesse o cadastro do **Sindicato** (Pessoal+ > Cadastros), aba [Convenção Coletiva, Acordo Coletivo ou Sentença Normativa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953-Sindicato#AbaConven%C3%A7%C3%A3ocoletiva,AcordocoletivoouSenten%C3%A7aNormativa) e preencha os dados da convenção coletiva:

- **Data Base**;
- **Data Assinatura**;
- **Percentual** de reajuste;
- **Ref. Reajuste** (período de diferença);
- Informações do **Processo** (quando houver).

  | **⚠️** **Atenção**  Sem essas informações, o sistema não consegue identificar o período do dissídio. |
  | --- |

**(4)** **Reajuste Salarial**

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:** br.com.sankhya.rh.ReajusteSalarial

1. Execute o [reajuste salarial](https://ajuda.sankhya.com.br/hc/pt-br/articles/40242689587095).

   | **⚠️** **Atenção**  O dissídio depende diretamente do novo salário definido no reajuste. |
   | --- |

**(1)** **Configurações relacionadas**

- Parâmetro **Usa valores recalculados na fbe/fbedtpag para dissidio? - FPCALCDISSMEM**.

  Este parâmetro define como as funções **FBE** e **FBEDTPAG** obtêm os valores de outras folhas durante o recálculo do dissídio.

  - Quando habilitado, o sistema utiliza os valores efetivamente recalculados em memória das folhas envolvidas no processo, garantindo maior precisão em cálculos que dependem de tabelas de faixas, como **INSS**, **IRRF** e demais tributos calculados sobre diferenças apuradas no dissídio.
  - Quando desabilitado, o sistema mantém o comportamento anterior, utilizando os valores corrigidos apenas pelo percentual de reajuste aplicado pelo dissídio.

    | 💡 **Dica**  Recomenda-se habilitar este parâmetro para que os impostos e bases dependentes de faixas sejam calculados com base nos valores efetivamente recalculados, evitando divergências na apuração de diferenças de INSS, IRRF e demais encargos em folhas complementares de dissídio. |
    | --- |

### Jornada de Uso

Após realizar o reajuste sindical, calcule a folha de dissídio.

**(1)** A tela de **Cálculos**(Pessoal+ > Rotinas Folha) pode ser acessada de duas maneiras:

1. Pela barra de pesquisa do Sankhya Om;

![Imagem 1: Pela barra de pesquisa do Sankhya Om;](https://ajuda.sankhya.com.br/hc/article_attachments/40299736728343)

2. Pelo **Gerenciador de DP** (Pessoal+ > Rotinas Folha), clicando sobre o menu **Cálculos**.

![Imagem 2: Pelo Gerenciador de DP (Pessoal+ > Rotinas Folha), clicando sobre o menu Cálculos .](https://ajuda.sankhya.com.br/hc/article_attachments/40299736728599)

**(2)**  O cálculo de folha adiantamento pode ser realizado de duas formas:

- coletiva;
- individual.

Clique sobre a opção desejada.

![Imagem 3: Clique sobre a opção desejada.](https://ajuda.sankhya.com.br/hc/article_attachments/40299736728855)

1. Selecione o **Tipo de folha Dissídio**;
2. Preencha as informações conforme o tipo de cálculo;
3. Clique em **Calcular**.

   Após o cálculo, a folha complementar será gerada com as diferenças.

   O sistema executa automaticamente:

   - **Reprocessamento dos meses anteriores**:
     - Identifica os períodos afetados pela CCT;
     - Recalcula os eventos com o novo salário.
   - **Aplicação do percentual de reajuste com base na regra de cálculo:**
     - Aplica percentual em todos os eventos configurados;
     - Respeita tipo de colaborador (mensalista ou não).
   - **Recálculo das bases:**
     - INSS recalculado por competência;
     - IRRF ajustado conforme diferenças;
     - FGTS recalculado automaticamente.
   - **Separação por referência (os valores são apresentados com):**
     - Referência de origem;
     - Valores originais;
     - Diferenças apuradas.
4. Após calcular, valide:

   - **Proventos**

     - Diferenças agrupadas por evento;
   - **Descontos**

     - INSS recalculado;
     - IRRF correto;
   - **Bases**

     - Base de INSS;
     - Base de FGTS;
     - Base de IRRF;
   - **Detalhamento**

     - Referência de origem visível;
     - Memória de cálculo disponível.
5. Após a conferência, o sistema considera o cálculo concluído.
6. Confirme a folha.
7. Acesse **Documentos** para:
   - Emitir holerite;
   - Disponibilizar ao colaborador;
8. Acesse [**Gerenciador de Folhas**](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247) para:
   - Integração contábil;
   - Integração financeira;
   - Liberação para o eSocial;

### Pontos de Atenção

- O reajuste salarial é pré-requisito obrigatório.
- Eventos e bases devem estar corretamente configurados.
- A ordem do processo impacta diretamente o resultado.
- Diferenças podem envolver meses anteriores.

### Perguntas Frequentes (FAQ)

**1. Por que o evento de dissídio não aparece no cálculo?**

Verifique se:

- o evento está ativo;
- o evento possui incidência correta;
- o campo **Tem seus valores recalculados** está marcado;
- existe um **Evento de Diferença/RRA** vinculado;
- o reajuste salarial foi efetivado antes do cálculo da folha de dissídio.

Também valide se o evento está configurado para cálculo complementar nas bases de INSS, IRRF e FGTS.

**2. Por que o reajuste sindical não foi aplicado para todos os colaboradores?**

Isso pode ocorrer quando:

- existem colaboradores admitidos após a data-base;
- o salário já está acima do piso sindical;
- o colaborador possui situação incompatível para o reajuste;
- a opção de readequação ao piso não foi marcada;
- o campo **Ref. Salário Base** do sindicato está incorreto.

Confira também se todos os colaboradores foram selecionados na etapa de efetivação.

**3. O sistema não recalculou os eventos após o reajuste. O que fazer?**

Após efetivar o reajuste salarial, é necessário:

1. recalcular a folha de dissídio;
2. conferir se os eventos possuem incidência complementar;
3. validar se a regra de cálculo da empresa permite recalcular todos os eventos da folha complementar.

Sem essas configurações, alguns eventos podem não sofrer reajuste automaticamente.

**4. Por que o valor do dissídio ficou zerado?**

As causas mais comuns são:

- percentual de reajuste incorreto;
- salário atual já compatível com o piso;
- evento sem vínculo de diferença/RRA;
- período da convenção configurado incorretamente;
- colaborador fora da vigência da convenção.

Também pode ocorrer quando a folha já foi recalculada anteriormente e não existem mais diferenças a pagar.

**5. Por que o sistema apresenta divergência no cálculo do adicional noturno ou horas extras no dissídio?**

Eventos variáveis dependem de:

- incidência correta no cadastro do evento;
- composição correta das bases;
- configuração da regra de cálculo complementar;
- existência das movimentações originais na folha de origem.

Quando essas configurações não estão alinhadas, os reflexos podem ser calculados incorretamente.

**6. O reajuste salarial pode ser aplicado para colaboradores demitidos?**

Sim.

Para isso, marque a opção **Aplicar reajuste para demitidos entre data-base e assinatura**.

Também é possível considerar colaboradores com aviso prévio indenizado projetado dentro do mês da data-base.

**7. Por que o sistema bloqueia um novo reajuste sindical?**

O bloqueio ocorre quando existe:

- sequência de reajuste anterior não aplicada;
- parcela de CCT pendente;
- reajuste posterior já efetivado.

Nesses casos, o sistema exige que a sequência cronológica seja respeitada.

**8. Por que o cálculo do dissídio apresenta diferença apenas em alguns colaboradores?**

Isso normalmente acontece porque:

- os colaboradores possuem salários diferentes;
- existem admissões após a data-base;
- houve alteração salarial manual;
- alguns colaboradores possuem afastamentos;
- nem todos estavam vinculados ao sindicato correto;
- a opção **Considerar mês de admissão independente dos dias trabalhados** não está habilitada na tela **Regras de Cálculo** (aba Propriedades > Geral > Reajuste Sindical), o que pode gerar inconsistências para colaboradores admitidos durante o período de referência.

**9. O que fazer quando o INSS complementar está incorreto?**

Confira:

- se as bases de INSS estão marcadas como complementar;
- se a referência de origem foi informada corretamente;
- se existem verbas de meses anteriores;
- se houve alteração manual em movimentos.

No caso de verbas retroativas, o sistema recompõe a base conforme orientação do eSocial.

**10. Por que o IRRF do dissídio ficou diferente do esperado?**

O IRRF pode variar devido a:

- cálculo de RRA;
- quantidade de meses considerados;
- diferenças de 13º salário;
- incidência tributária dos eventos.

Quando existem valores de anos anteriores, o cálculo ocorre de forma separada conforme regras de RRA.

**11. O sistema permite lançar diferenças manualmente?**

Sim.

Na tela **Lançamento de Movimento**, utilize:

- tipo de movimento **Dissídio**;
- ou **Verbas de Meses Anteriores**.

Nesses casos, informe obrigatoriamente a referência de origem.

**12. Por que o evento lançado manualmente não aparece no cálculo?**

Verifique:

- se a folha foi recalculada;
- se o movimento está confirmado;
- se a referência de origem é válida;
- se o evento está ativo;
- se existe bloqueio por folha já confirmada.

**13. O reajuste salarial altera automaticamente folhas já calculadas?**

Não.

Após efetivar o reajuste, é necessário recalcular:

- folha mensal;
- folha de dissídio;
- rescisão complementar, quando aplicável.

**14. Como validar se o reajuste foi enviado corretamente ao eSocial?**

Após confirmar a folha:

1. acesse o Gerenciador de Folhas;
2. realize a liberação para o eSocial;
3. acompanhe os eventos S-1200, S-1210 e S-2206;
4. valide o registro de envio para o eSocial no cadastro do colaborador.

**15. Por que o sistema apresenta diferenças pequenas de centavos no dissídio?**

Diferenças pequenas geralmente ocorrem devido a:

- regras de arredondamento;
- cálculo proporcional;
- médias variáveis;
- diferenças entre mês comercial e mês real.

Revise os tipos de arredondamento configurados para mensalistas e não mensalistas.

**16. O que acontece se eu cancelar um reajuste já efetivado?**

Ao cancelar:

- os cálculos relacionados devem ser refeitos;
- reajustes posteriores podem ser invalidados;
- a sequência da convenção coletiva volta a ser validada.

Por isso, sempre confira os valores antes da efetivação.

**17. Por que o sistema não permite excluir um evento de RRA?**

Eventos de RRA vinculados a outros eventos não podem ser excluídos enquanto houver relacionamento ativo.

Primeiro é necessário remover os vínculos de diferença/RRA existentes.

**18. Como conferir os valores calculados no dissídio?**

A conferência pode ser feita:

- na tela Cálculos;
- no Gerenciador de Folhas;
- no Resumo da Folha;
- nas bases de composição;
- nos logs de cálculo.

Confira principalmente:

- valor original;
- percentual aplicado;
- referência de origem;
- incidências tributárias;
- bases de INSS e IRRF.

**19. Quando utilizar Verbas de Meses Anteriores ao invés de Dissídio?**

Utilize:

- **Dissídio**: para diferenças relacionadas à Convenção Coletiva;
- **Verbas de Meses Anteriores**: para pagamentos retroativos que não dependem de CCT.

**20. O que pode impedir o cálculo da folha complementar?**

Os principais fatores são:

- eventos sem incidência complementar;
- sindicato sem convenção configurada;
- reajuste salarial não efetivado;
- ausência de vínculo RRA;
- folha já confirmada;
- referências inconsistentes.

Sempre valide as configurações antes de iniciar o cálculo.

### Artigos Relacionados

- [Reajuste Salarial](https://ajuda.sankhya.com.br/hc/pt-br/articles/4424998383767)
- [Rendimentos Recebidos Acumuladamente (RRA)](https://ajuda.sankhya.com.br/hc/pt-br/articles/15696666423319)
- [Cadastro de Sindicato](https://ajuda.sankhya.com.br/hc/pt-br/articles/360058937953)
- [Cadastro de Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/33041194565911)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
