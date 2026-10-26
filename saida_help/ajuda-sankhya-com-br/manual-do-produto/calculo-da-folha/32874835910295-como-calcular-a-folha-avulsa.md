---
id: "32874835910295"
titulo: "Como calcular a folha avulsa"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Cálculo da Folha"
atualizado_em: "2026-10-02T15:35:33Z"
rotulos: ["Configuração", "Relatórios", "avulsa", "eSocial", "ID: br.com.sankhya.rh.CalculoIndFolha", "Folha de Pagamento", "Lançamento de Movimento", "Pessoal+ » Rotinas Folha » Cálculos", "Folha avulsa", "Pessoal+", "FPRECIBOFOLAVU"]
---

# Como calcular a folha avulsa

**Módulo:** Pessoal+                                          

**Versão mínima:** 5.36

**Caminhos de acesso:**

1. Painel de configurações (Pessoal+ > Configurações > Painel de Configurações)
2. Eventos (Pessoal+ > Cadastros > Eventos)
3. Lançamento de movimento (Pessoal+ > Rotinas Folha > Lançamento de Movimento)
4. Cálculos (Pessoal+ > Rotinas Folha > Cálculos)

---

## Sumário

[Descrição e Usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JYRSHEA47DN2ARPJMPBAAK5J)

1. [Descrição](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01HA7B8E3FQG6AQ73CZ3Z4J3C5)
2. [Pré-requisitos](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JY6MMN9K2XQ17EEG4TAA3E1J)
3. [Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JY6G2G35EK6T62B0DYM3RCCZ)
4. [Jornada de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JXZD26W5467K5JX25EQ46AT1)
5. [Ponto de atenção](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JY6G3YYX358XHFEX7M9RDGT0)
6. [Dicas de usabilidade](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JXZD26WHDATS0Q60K45PGVJJ)
7. [Casos de uso](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JXZD26WN07MF3X3R7TB6Q3A4)

[Perguntas frequentes (FAQ)](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JXZD26WS16MD2RV6DQZ3KG9X)

[Artigos relacionados](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-Como-calcular-a-folha-avulsa#h_01JY6MFXR43YR051W1QRBKC7VM)

---

## Descrição e Usabilidade

### 1. Descrição

 A **Folha Avulsa** permite lançar e calcular pagamentos específicos para um colaborador em uma competência (mês), **sem impactar a folha mensal padrão**. 

Ela é útil para pagamentos de valores pontuais, como **horas extras, comissões** ou outros pagamentos que precisam ser processados **fora do ciclo mensal regular**. 

Essa funcionalidade facilita o controle financeiro e evita erros de duplicidade, pois os valores lançados na folha avulsa são **automaticamente considerados** na folha mensal do colaborador.

### 2. Pré-requisitos

#### **(1)** Regras da folha avulsa

Antes de iniciar o cálculo, é fundamental entender as regras de funcionamento da **folha avulsa**:

- **Uma única folha avulsa por colaborador por competência**: não é permitido lançar mais de uma folha avulsa para o mesmo colaborador no mesmo mês.
- **Incompatível com folha mensal ou rescisão já calculadas**: se já houver cálculo mensal ou rescisório na mesma competência, não será possível gerar a folha avulsa.
- **Sem envio ao eSocial nesta versão**: a folha avulsa ainda **não possui tributação própria** e, por isso, **não é enviada ao eSocial**.
- **Valores recalculados na folha mensal**: os eventos lançados na folha avulsa serão **recalculados na folha mensal**, e o valor já pago será **descontado automaticamente** para evitar duplicidade.

#### **(1)** Permissões necessárias

1. Acesse o **Painel de Configurações** (Pessoal+ > Configurações > Painel de Configurações).
2. Vá até a seção **Configuração de Permissões**.
3. Selecione a tela **Cálculos**, em seguida, o grupo de usuários desejado e certifique-se de que a permissão **Realizar cálculos avulsos** esteja habilitada para permitir o uso da funcionalidade da folha avulsa.

[GIF animado: Imagem 1: Selecione a tela Cálculos , em seguida, o grupo de usuários desejado e certifique-se de que a permissão Realizar…](https://ajuda.sankhya.com.br/hc/article_attachments/32938547188631)

####

#### **(1)** Configurações prévias

(1)** Eventos**

Certifique na tela **Eventos** (Pessoal+ > Cadastros > Eventos) que os eventos que você precisa estão configurados para a folha avulsa.

Os tipos de eventos permitidos, ou seja, eventos com **gatilho por lançamento de movimento**, são:

- **horas extras;**
- **comissões;**
- **DSR sobre comissões ou horas extras.**

Caso precise criar um novo evento:

- é possível **copiar eventos existentes** e **duplicar** para uso em folha avulsa;
- o evento deve ser acionado apenas por **lançamento de movimento**;
- **não marque** o evento como parte de regras automáticas de cálculo para outros tipos de pagamento (mensal, férias);

![Imagem 2: não marque o evento como parte de regras automáticas de cálculo para outros tipos de pagamento (mensal, férias);](https://ajuda.sankhya.com.br/hc/article_attachments/32938744585495)

- verifique se o evento **possui reflexos**, como DSR, e se estes também estão corretamente configurados.

(2)** Lançamento de movimento**

1. Acesse a rotina de **Lançamento de movimento** (Pessoal+ > Rotinas Folha > Lançamento de Movimento) e crie um lançamento do tipo de folha **Avulsa**.
2. Selecione o funcionário, e na aba Lançamento, escolha o tipo de folha como **Avulso**.
3. Escolha o **evento desejado**.
4. Informe o **valor** ou **índice** conforme o caso.
5. Salve o lançamento e confira pela aba Visualização.

   ![Imagem 3: Salve o lançamento e confira pela aba Visualização.](https://ajuda.sankhya.com.br/hc/article_attachments/32939312524823)

📚 Para mais detalhes, consulte o artigo: [Lançamento de Movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/38268572935319).

**(3)**  **Relatório de Holerite da Folha Avulsa**

Caso deseje utilizar um layout específico para o holerite da Folha Avulsa, configure o parâmetro **Holerite Folha Avulsa - FPRECIBOFOLAVU** com o código de um relatório cadastrado na tela **Relatórios Formatados**.

- Quando o parâmetro estiver preenchido, o sistema utilizará o relatório informado para emitir os holerites da Folha Avulsa.
- Quando o parâmetro não estiver preenchido, será utilizado automaticamente o mesmo modelo de holerite configurado para a folha mensal.

### 3. Diagrama de fluxo

![Imagem 4: 3. Diagrama de fluxo](https://ajuda.sankhya.com.br/hc/article_attachments/32895527154199)

### 4. Jornada de uso

#### **(1)** Calcular Folha avulsa

1. Após o lançamento dos eventos, acesse a tela de **cálculo** (Pessoal+ > Rotinas Folha > Cálculos).
2. Clique no card **Avulsa**.
    ![Imagem 5: Clique no card Avulsa .](https://ajuda.sankhya.com.br/hc/article_attachments/32938929060503)
3. Informe a **referência** e **data de pagamento**.
4. Selecione o(s) funcionário(s) desejado(s).
5. Execute o cálculo (**individual ou coletivo**) e confirme a folha.

![Imagem 6: Execute o cálculo ( individual ou coletivo ) e confirme a folha.](https://ajuda.sankhya.com.br/hc/article_attachments/32939329114903)

**Observações**

- A folha avulsa **não terá tributação automática**.
- É possível **personalizar fórmulas de provisão**, caso deseje calcular descontos legais como INSS ou IRRF.

#### **(2)** Calcular folha mensal

Depois, calcule normalmente a folha mensal do colaborador, assim:

- os eventos pagos na folha avulsa serão recalculados para gerar as bases de INSS, FGTS e IRRF;
- o valor líquido já pago na folha avulsa será descontado automaticamente do total da folha mensal.

#### **(3)**  Emitir Holerite da Folha Avulsa

Depois de confirmar o cálculo da Folha Avulsa, é possível emitir o recibo individual ou coletivo.

(3)**Emissão individual**

Na tela **Cálculos** (Pessoal+ > Rotinas Folha), selecione o colaborador calculado e utilize a opção **Emitir Holerite**.

**(3)Emissão coletiva**

Na tela **Gerenciador de Folhas**, marque a opção **Ativa Seleção**, selecione os colaboradores desejados e utilize a opção **Emitir Holerite**.

O sistema:

- gera os recibos em PDF ou envia os holerites por e-mail, seguindo o fluxo padrão do sistema;
- gera o recibo utilizando:

  - o relatório configurado no parâmetro **FPRECIBOFOLAVU**, quando informado;
  - ou o modelo padrão utilizado para a folha mensal, caso o parâmetro não esteja configurado.

### 5. Pontos de atenção

- Só é possível gerar **uma folha avulsa por colaborador dentro da mesma competência**.
- A folha avulsa só poderá ser calculada se não houver cálculo mensal ou de rescisão realizado para a referência.
- A folha avulsa **não gera tributação, nem é enviada ao eSocial** nesta versão.
- Os eventos pagos na folha avulsa serão recalculados na folha mensal para tributação e o valor será descontado.
- Após cálculo e integração financeiro e contábil, não será possível editar os cálculos da folha avulsa.
- O parâmetro **FPRECIBOFOLAVU** permite definir um modelo exclusivo de holerite para a Folha Avulsa:
  - quando não estiver configurado, será utilizado automaticamente o mesmo relatório da folha mensal;
  - o relatório informado deve estar previamente cadastrado na tela **Relatórios Formatados**.

### 6. Dicas de usabilidade

- Use filtros para selecionar apenas os funcionários necessários ao calcular a folha avulsa.
- Sempre confirme a referência (competência) antes de lançar e calcular para evitar erros.
- Utilize o símbolo identificador na folha mensal para conferir eventos pagos via folha avulsa.

### 7. Casos de uso

- Pagamento de horas extras fora do fechamento mensal.
- Pagamento de comissões pontuais.
- Ajustes isolados em valores específicos para um colaborador.
- Regularização de pagamentos que não puderam ser incluídos na folha mensal.

## Perguntas frequentes (FAQ)

**1.** **Posso lançar mais de uma folha avulsa para o mesmo colaborador no mesmo mês?**

Não. Apenas uma folha avulsa por colaborador por competência é permitida.

**2. A folha avulsa gera encargos e contribuições?**

Não, a tributação é feita na folha mensal ou rescisão quando os eventos são recalculados.

**3. Posso editar um lançamento na folha avulsa depois do cálculo?**

Após o cálculo e integração financeira, os lançamentos ficam bloqueados para edição.

**4. O que acontece se eu calcular a folha mensal antes da folha avulsa?**

A folha mensal não reconhecerá os valores pagos na folha avulsa e poderá gerar pagamento duplicado.

**5.** **A folha avulsa é um complemento da folha ou um adiantamento?**

A folha avulsa é um tipo de pagamento flexível que pode ser utilizada tanto como complemento da folha principal quanto como adiantamento salarial em diferentes situações. 

É importante destacar que os proventos pagos por meio da folha avulsa serão incluídos no cálculo da folha mensal regular, e o valor já antecipado será descontado para evitar pagamentos duplicados.

**6.** **Posso pagar só 72,5% do valor como adiantamento e reservar 27,5% para impostos da folha mensal?**

Sim. Basta **cadastrar e configurar um evento** para provisionar os descontos na folha avulsa.

**7.** **Qual letra identifica a folha avulsa em relatórios, arquivo de remessa e lançamento de movimento?**

A letra que representa a folha avulsa em todas as tabelas é **"V"** e o nome do campo que a identifica é **TIPFOLHA**.

**8.** **O cálculo da folha avulsa provisiona valores de desconto de INSS e IRRF?**

Nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**9. Como é a integração contábil da folha avulsa?**

Segue o mesmo processo das demais folhas, sem alterações.

**10. A folha avulsa faz desconto de crédito do trabalhador (empréstimos)?**

Nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**11. Posso pagar comissões na folha avulsa? O DSR, INSS e IR serão calculados?**

Sim, para comissões. Contudo, nativamente, não há eventos configurados para descontos na folha avulsa, mas existe a possibilidade de cadastrar e configurar um evento para provisionar descontos.

**12. A folha avulsa é enviada para o eSocial?**

Não há envio para o eSocial.

**13.** **Posso usar a folha avulsa para pagar um funcionário demitido?**

Não. Para isso, use a rescisão complementar.

**14.** **A folha avulsa tem incidência de impostos?**

Não. A tributação é recalculada na folha mensal.

**15. Posso utilizar um holerite diferente para a Folha Avulsa?**

Sim. Basta configurar o parâmetro **FPRECIBOFOLAVU (Holerite Folha Avulsa)** com o código de um relatório cadastrado em **Relatórios Formatados**.

Caso o parâmetro não seja informado, o sistema utilizará automaticamente o mesmo modelo de holerite da folha mensal.

## Artigos relacionados

- [Painel de configurações](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559)
- [Eventos](https://ajuda.sankhya.com.br/hc/pt-br/articles/4405026143767)
- [Lançamento de movimento](https://ajuda.sankhya.com.br/hc/pt-br/articles/13968004985495)
