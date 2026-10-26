---
id: "39369772802327"
titulo: "Como o sistema calcula a licença remunerada nas férias coletivas?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39369772802327-Como-o-sistema-calcula-a-licen%C3%A7a-remunerada-nas-f%C3%A9rias-coletivas"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:29:16Z"
rotulos: ["Folha de Pagamento", "Férias Coletivas", "Configuração Funcionários", "Recibo de Férias", "Artigo criado KCS", "Sankhya RH - KCS", "Licença Remunerada"]
---

# Como o sistema calcula a licença remunerada nas férias coletivas?

Durante o cálculo de **"Férias Coletivas"**, o sistema Sankhya possui um comportamento específico para funcionários que não possuem saldo suficiente de dias de férias. Quando o colaborador tem menos de 10 dias de saldo disponível para gozo, o sistema automaticamente calcula a diferença como **"Licença Remunerada"** e a inclui no recibo de férias, em vez de lançá-la na folha mensal.

Este é o comportamento padrão do sistema atualmente. Embora a **"Licença Remunerada"** apareça no cálculo das férias, não há inconsistências contábeis, pois os valores são processados corretamente para fins de pagamento e encargos.

### Comportamento do sistema no cálculo

Quando um funcionário é incluído nas **"Férias Coletivas"** e não possui dias suficientes no período aquisitivo, o sistema realiza automaticamente a seguinte divisão:

- Os dias disponíveis no período aquisitivo são calculados como **"Férias Normais"**
- Os dias restantes para completar o período de **"Férias Coletivas"** são calculados como **"Licença Remunerada"**
- Ambos os valores aparecem no **"Recibo de Férias"** do colaborador

Por exemplo: se as **"Férias Coletivas"** são de 14 dias e o funcionário possui apenas 12,5 dias de direito, o sistema calculará 12,5 dias como **"Férias"** e 1,5 dia como **"Licença Remunerada"**.

### Solução para recálculo incorreto

Se o sistema estiver calculando todos os dias como **"Licença Remunerada"** quando deveria dividir entre férias e licença, execute o recálculo das férias coletivas. Em alguns casos, o sistema armazena cache de cálculo que precisa ser limpo.

Para calcular utilize a tela de **"Cálculos"** (Pessoal+ » Rotinas Folha » Cálculos), aba -> coletivo -> Férias insira as informações

![Imagem 1: Para calcular utilize a tela de "Cálculos" ( Pessoal+ » Rotinas Folha » Cálculos ), aba -> coletivo -> Férias insira as…](https://ajuda.sankhya.com.br/hc/article_attachments/41354808375447)

![Imagem 2: Para calcular utilize a tela de "Cálculos" ( Pessoal+ » Rotinas Folha » Cálculos ), aba -> coletivo -> Férias insira as…](https://ajuda.sankhya.com.br/hc/article_attachments/41354782026775)

**Para excluir** o colaborador com inconsistência, utilize a rotina: **''Gerenciador de folhas'' (**Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e inclua a referência e empresa para localizar o funcionário 

Exclua o cálculo atual das **"Férias Coletivas"** para o funcionário.

 Execute novamente o cálculo das **"Férias Coletivas"** para o colaborador.

 Verifique se agora o sistema dividiu corretamente entre dias de **"Férias"** e dias de **"Licença Remunerada"**.

### Personalização do recibo de férias

Caso seja necessário que a **"Licença Remunerada"** não apareça no **"Recibo de Férias"**, é possível personalizar o layout do recibo. Esta personalização permite ocultar a verba de **"Licença Remunerada"** do documento impresso, mantendo o cálculo correto no sistema.

Para solicitar esta personalização, entre em contato com a equipe responsável por relatórios personalizados (unidade ou solicitação em chamado via Service Desk), informando a necessidade de ajustar o layout do **"Recibo de Férias"** ante esta especificidade.

**Importante:** Mesmo com a **"Licença Remunerada"** sendo calculada junto às férias, não há inconsistências contábeis ou fiscais, pois os valores e encargos são processados corretamente pelo sistema.
