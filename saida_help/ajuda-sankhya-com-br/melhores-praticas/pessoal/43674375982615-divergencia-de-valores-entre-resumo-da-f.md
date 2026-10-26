---
id: "43674375982615"
titulo: "Divergência de valores entre resumo da folha e eSocial: como identificar e corrigir?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43674375982615-Diverg%C3%AAncia-de-valores-entre-resumo-da-folha-e-eSocial-como-identificar-e-corrigir"
trilha: "Melhores Práticas > Pessoal+"
atualizado_em: "2026-10-07T14:39:13Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Divergência de valores entre resumo da folha e eSocial: como identificar e corrigir?

A divergência de valores entre o **"Resumo da Folha"**  e o **"eSocial"** é uma dúvida frequente entre profissionais de departamento pessoal e contabilidade. Essas diferenças podem ocorrer em bases de INSS, FGTS, IRRF e outros encargos, gerando dúvidas sobre qual valor está correto e como proceder para garantir a conformidade fiscal e evitar problemas futuros.

### Quais as principais causas das divergências?

As principais causas de divergência entre o resumo da folha e o eSocial são:

**(1)** **Diferença nos valores das bases de cálculo:** O sistema pode considerar uma base de cálculo diferente daquela utilizada pelo eSocial. Isso ocorre porque o eSocial realiza seus próprios cálculos com base nas **incidências cadastradas nas rubricas enviadas anteriormente**.

**(2)** **Folhas não enviadas ao eSocial:** Quando folhas de **adiantamento, férias ou rescisão** não são devidamente enviadas ou processadas pelo eSocial, seus valores não são considerados nos totalizadores, podendo gerar divergências em relação ao Resumo da Folha.

**(3)** **Parâmetros de incidência incorretos:** Eventos/rubricas com parametrização incorreta de incidência para **INSS, FGTS ou IRRF** podem fazer com que os valores calculados pelo sistema sejam diferentes dos valores considerados pelo eSocial.

**(4)** **Reenvio ou retificação pendente:** Alterações realizadas após o envio inicial, como ajustes de incidência, valores ou inclusão de eventos, podem exigir o **reenvio ou a retificação dos eventos S-1200 e S-1210**, para que as informações atualizadas sejam consideradas pelo eSocial.

### Como identificar e corrigir as divergências?

Para identificar a origem da divergência e realizar as devidas correções, siga os passos abaixo:

**(1)** **Compare as bases de cálculo:** Compare as bases de **INSS, FGTS e IRRF** apresentadas no **Resumo da Folha** com os valores apresentados no portal do eSocial. Para isso basta acessar a tela  Gerenciador de Folhas (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e gerar o **"Resumo da Folha".** E Verifique se os valores das bases calculadas pelo sistema correspondem aos valores considerados pelo eSocial.

**(2)** **Utilize as telas de conferência:** O sistema disponibiliza telas específicas para auxiliar na identificação das diferenças. Acesse as opções conforme o tributo que apresenta divergência:

- **Conferência IRRF** - Tela S-5002 - Conferência IRRF (Pessoal+ » Consultas » S-5002 - Conferência IRRF).
- **Conferência INSS/PIS** - Tela S-5001 - Conferência INSS/PIS (Pessoal+ » Consultas » S-5001 - Conferência INSS/PIS).
- **Conferência FGTS** - Tela S-5003 - Conferência FGTS (Pessoal+ » Consultas » S-5003 - Conferência FGTS).

Essas telas permitem **detalhar e comparar os valores apurados pelo sistema e pelo eSocial**, facilitando a identificação dos **trabalhadores, eventos ou rubricas** que estão gerando a divergência.

**(3)** **Analise a origem da diferença:** Necessário localizar o funcionário e posteriormente o evento que esta causando a diferença. 

**(4)** Para avaliar o evento e, se necessário, realizar os ajustes, acesse a tela **Eventos** (Pessoal+ » Cadastros » Eventos) e verifique as abas **Avançado**, **eSocial** e **Bases de Cálculo**.

As configurações dessas abas influenciam diretamente o cálculo realizado pelo sistema e as informações enviadas ao eSocial. Portanto, é importante garantir que os eventos estejam corretamente parametrizados para evitar divergências entre a folha de pagamento e os valores apresentados pelo eSocial.

Na aba **Avançado** e em **Bases de Cálculo**, as configurações definem como o evento será considerado no cálculo da folha.

Por exemplo, o campo **INSS**, na aba **Avançado**, determina se o evento irá ou não compor a base de INSS e referente a qual tipo de folha, isso vale também para as outras incidências, o campo IRRF e campo Outros (determina FGTS). Após realizar um ajuste nesse campo, é importante conferir se a configuração correspondente também está refletida na aba **Bases de Cálculo**.

Assim, ao configurar o campo **INSS** como **INSS**, a respectiva base, como a **Base de INSS (1901)**, deve estar corretamente vinculada na aba **Bases de Cálculo**. Processe necessário também para as demais bases de IRRF e FGTS de acordo com cada tipo de folha.

![Imagem 1: Assim, ao configurar o campo INSS como INSS , a respectiva base, como a Base de INSS (1901) , deve estar corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44065163709847)

![Imagem 2: Assim, ao configurar o campo INSS como INSS , a respectiva base, como a Base de INSS (1901) , deve estar corretamente…](https://ajuda.sankhya.com.br/hc/article_attachments/44065191309847)

As informações preenchidas na aba **eSocial** são enviadas ao eSocial para que as incidências sejam consideradas no cálculo interno.

É importante que essas configurações estejam **de acordo com o cálculo realizado pelo sistema**. Por exemplo, se um evento compõe a base de INSS, o campo **INSS** deve estar configurado com a incidência **11 – Mensal**.

Dessa forma, as incidências configuradas no sistema e enviadas ao eSocial permanecem consistentes, evitando divergências nos cálculos.

![Imagem 3: Dessa forma, as incidências configuradas no sistema e enviadas ao eSocial permanecem consistentes, evitando…](https://ajuda.sankhya.com.br/hc/article_attachments/44065163712791)

Caso seja identificada alguma divergência, será necessário realizar a correção de acordo com a origem do problema.

- **Ajustes nas abas Avançado e Bases de Cálculos:** é necessário **recalcular a folha** para que a alteração seja aplicada ao cálculo e ao resumo da folha. Após o recálculo, é necessário **reenviar o evento S-1200** ao eSocial.
- **Ajustes na aba eSocial:** é necessário **enviar o evento S-1010** com a nova configuração da rubrica. Antes do envio, verifique a **data de início de validade da rubrica**. Após o processamento do S-1010, será necessário **reenviar o S-1200**.

**Atenção:** caso o ajuste seja realizado na **incidência de IRRF**, será necessário enviar o evento **S-1010** e, posteriormente, o **S-1210**. Não é necessário reenviar o **S-1200**, pois as informações de IRRF são enviadas no **S-1210**.

### Quais são as melhores práticas para evitar divergências?

Para evitar divergências entre os valores apresentados no **Resumo da Folha** e os valores considerados pelo **eSocial**, é importante adotar alguns cuidados durante a parametrização dos eventos, o processamento da folha e o envio das informações ao eSocial.

- **Mantenha os eventos corretamente parametrizados:** as incidências definidas na aba **Avançado** e as respectivas bases vinculadas na aba **Bases de Cálculo** devem estar de acordo com as informações configuradas na aba **eSocial**. Essa consistência é fundamental para que o cálculo realizado pelo sistema esteja alinhado ao cálculo interno realizado pelo eSocial.
- **Envie o S-1010 antes dos eventos S-1200 e S-1210:** sempre que houver alteração nas incidências dos eventos, envie o **S-1010** com a nova configuração da rubrica antes de realizar o envio dos eventos **S-1200 e S-1210**.
- **Confira as folhas antes do fechamento:** certifique-se de que as folhas de **mensal, adiantamento, férias e rescisão**, quando aplicáveis, foram devidamente liberadas e enviadas ao eSocial.
- **Realize conferências periódicas:** utilize o **Resumo da Folha** em conjunto com as telas de conferência **S-5001, S-5002 e S-5003** para identificar possíveis diferenças.
- **Evite alterações após o envio sem realizar as devidas retificações:** caso seja necessário alterar uma incidência ou outra informação que já tenha sido enviada ao eSocial, avalie quais eventos precisam ser reenviados ou retificados para que os dados permaneçam consistentes.

Adotar essas práticas contribui para manter as informações da **folha de pagamento e do eSocial alinhadas**, reduzindo a ocorrência de divergências e facilitando a identificação e correção de inconsistências antes do fechamento das obrigações.
