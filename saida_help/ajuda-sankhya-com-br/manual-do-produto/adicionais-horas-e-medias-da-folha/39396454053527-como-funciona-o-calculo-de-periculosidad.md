---
id: "39396454053527"
titulo: "Como funciona o cálculo de periculosidade?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39396454053527-Como-funciona-o-c%C3%A1lculo-de-periculosidade"
trilha: "Manual do Produto > Pessoas+ > Folha Mensal > Adicionais, Horas e Médias da Folha"
atualizado_em: "2026-09-27T17:46:37Z"
rotulos: ["Configuração", "Cálculo", "CLT", "Folha de Pagamento", "Artigo criado KCS", "Sankhya RH - KCS", "Adicional de Periculosidade"]
---

# Como funciona o cálculo de periculosidade?

O adicional de periculosidade é um direito garantido aos trabalhadores que exercem atividades em condições perigosas. Conforme previsto no art. 193, §1º da Consolidação das Leis do Trabalho, o percentual padrão do adicional é de 30% sobre o salário-base do empregado.

**No entanto, esse percentual pode ser diferente caso exista previsão específica em convenção coletiva (CCT) ou acordo coletivo firmado pelo sindicato da categoria.**

###

### Base de cálculo e percentual aplicado

O adicional de periculosidade é calculado, em regra, aplicando-se o percentual de 30% sobre o salário-base do colaborador, sem incluir prêmios, gratificações ou participações. Entretanto, esse percentual pode variar conforme previsão em convenção coletiva (CCT) ou acordo coletivo da categoria.

No sistema, a variável “PERCPERIC” é utilizada na fórmula do evento para aplicar automaticamente o percentual configurado para o cálculo do adicional de periculosidade.

Para verificar se o percentual está configurado corretamente, acesse a tela **"Configuração de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e consulte a aba de **"Contrato"** para validação do % Percentual cadastrado para o colaborador.

![Imagem 1: Para verificar se o percentual está configurado corretamente, acesse a tela "Configuração de Funcionários" (Pessoal+ »…](https://ajuda.sankhya.com.br/hc/article_attachments/40738222949399)

### Impacto das faltas no cálculo

O sistema considera que o adicional de periculosidade é devido sobre os dias efetivamente trabalhados, ou seja, quando há exposição ao risco. Nas hipóteses de faltas injustificadas, não há prestação de serviço nem exposição ao agente perigoso naquele(s) dia(s).

**Exemplo de cálculo com falta:**

• Salário-base: R$ 1.750,00
• Adicional de periculosidade (30%): R$ 525,00
• Dias do mês: 30
• Dias trabalhados: 20
• Dias de falta: 1

**• Base para cálculo proporcional: 19 dias**
**• Cálculo proporcional do adicional: R$ 525,00 ÷ 30 × 19 = R$ 332,50**

O desconto não decorre da alteração da base de cálculo prevista no art. 193 da CLT, mas sim da ausência do fato gerador (exposição ao risco) no período da falta. Este é o entendimento predominante na jurisprudência trabalhista.

### Correção de erros no cálculo

Quando o sistema não aplica corretamente o percentual de periculosidade ou apresenta valores inconsistentes, siga o procedimento abaixo para reprocessar o cálculo:

**(1)** Acesse a tela **"Cálculo"** (Pessoal+ » Rotinas Folha » Cálculos) e localize o colaborador com inconsistência.

**(2)** Exclua a folha mensal do colaborador referente ao período com erro.

**(3)** Acesse a tela **"Configuração de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários) e consulte a aba de **"Contrato"** para validação do % Percentual cadastrado para o colaborador. Caso haja divergência é necessário realizar o ajuste.

![Imagem 2: Acesse a tela "Configuração de Funcionários" (Pessoal+ » Cadastros » Configuração Funcionários), aba "Histórico" do…](https://ajuda.sankhya.com.br/hc/article_attachments/40738222949399)

**(4)** Acesse a tela **"Configuração de Funcionários"** (Pessoal+ » Cadastros » Configuração Funcionários), aba **"Histórico"** do colaborador, exclua a linha da referencia do calculo que não esta calculando o valor da periculosidade corretamente.

![Imagem 3: (4) Acesse a tela "Configuração de Funcionários" (Pessoal+ » Cadastros » Configuração Funcionários), aba "Histórico" do…](https://ajuda.sankhya.com.br/hc/article_attachments/40738222950679)

**(5)** Retorne à tela **"Cálculo"** e reprocesse o cálculo mensal do funcionário. E verifique se o valor do adicional de periculosidade foi calculado corretamente conforme esperado.

**Obs.:** Para cálculos retroativos, é necessário excluir a linha do histórico referente à competência em que deseja iniciar o recálculo. Caso contrário, o evento não será apurado na folha do colaborador.

**Vale lembrar que, ao excluir uma linha do histórico que possua informações anteriormente ajustadas, essas configurações serão perdidas. Ao salvar novamente o histórico, o sistema gravará os dados atuais que estiverem no cadastro do colaborador no momento.**

### Pagamento de diferenças via folha avulsa

Caso seja necessário pagar diferenças de periculosidade referentes a períodos anteriores, se necessário, faça a criação do evento de periculosidade para meses anteriores, e utilize a **"**[**Folha Avulsa**](https://ajuda.sankhya.com.br/hc/pt-br/articles/32874835910295-C%C3%A1lculo-da-folha-de-pagamento-avulsa)**".** Este tipo de folha permite o pagamento de verbas durante o mês, que posteriormente serão integradas à folha mensal para processamento dos encargos.

Os eventos lançados na folha avulsa serão recalculados na folha mensal, e o valor já pago será descontado automaticamente para evitar duplicidade. Para utilizar este recurso, acesse a tela **"Lançamento de Movimento"** (Pessoal+ » Rotinas Folha » Lançamento de Movimento) e selecione o tipo de folha **"Avulsa"**.

![Imagem 4: Os eventos lançados na folha avulsa serão recalculados na folha mensal, e o valor já pago será descontado…](https://ajuda.sankhya.com.br/hc/article_attachments/40739283495575)

É importante que a permissão “Realizar cálculos avulsos” esteja habilitada no [**Painel de Configurações**](https://ajuda.sankhya.com.br/hc/pt-br/articles/14999187265559-Painel-de-Configura%C3%A7%C3%B5es) (Pessoal+ » Configurações » Painel de Configurações).

No card “Configuração de Permissões”, selecione a opção “Cálculo”, escolha o grupo de decisores e, no lado direito da tela, serão apresentadas as permissões disponíveis. Localize a permissão referente à “Realizar cálculos avulsos” e deixe-a marcada para que a opção de cálculo fique disponível no sistema.

![Imagem 5: No card “Configuração de Permissões”, selecione a opção “Cálculo”, escolha o grupo de decisores e, no lado direito da…](https://ajuda.sankhya.com.br/hc/article_attachments/40738222951575)![Imagem 6: No card “Configuração de Permissões”, selecione a opção “Cálculo”, escolha o grupo de decisores e, no lado direito da…](https://ajuda.sankhya.com.br/hc/article_attachments/40738222952087)![Imagem 7: No card “Configuração de Permissões”, selecione a opção “Cálculo”, escolha o grupo de decisores e, no lado direito da…](https://ajuda.sankhya.com.br/hc/article_attachments/40738245904151)
