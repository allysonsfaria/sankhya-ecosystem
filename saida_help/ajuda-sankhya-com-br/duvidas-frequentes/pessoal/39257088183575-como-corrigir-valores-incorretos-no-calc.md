---
id: "39257088183575"
titulo: "Como corrigir valores incorretos no cálculo do DSR?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39257088183575-Como-corrigir-valores-incorretos-no-c%C3%A1lculo-do-DSR"
trilha: "Dúvidas Frequentes > Pessoal+"
atualizado_em: "2026-07-29T13:28:31Z"
rotulos: ["Configuração", "Eventos", "Feriados", "Folha", "DSR", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Como corrigir valores incorretos no cálculo do DSR?

O **"DSR (Descanso Semanal Remunerado)"** é calculado automaticamente pelo sistema com base em diversos fatores, como dias úteis trabalhados, dias não úteis, feriados cadastrados e a data de apuração do ponto. Quando o valor do DSR aparece incorreto, geralmente está relacionado a **"configurações desatualizadas"**, **"feriados cadastrados indevidamente"** ou **"parâmetros de apuração inadequados"**.

Este artigo apresenta as principais causas de valores incorretos no DSR e orienta sobre como identificar e corrigir cada situação.

###

### Feriados cadastrados incorretamente

O sistema considera os feriados cadastrados para calcular os dias não úteis que impactam o DSR. Se houver feriados cadastrados indevidamente ou faltando feriados válidos, o cálculo será afetado.

**Solução:**

**(1)** Acesse a tela **"Feriados"** (Pessoal+ » Cadastros » Feriados). 

**(2)** Verifique todos os feriados cadastrados para o período de apuração da folha. 

**(3)** Remova feriados que não são aplicáveis e inclua os feriados corretos que estejam faltando. 

**(4)** Recalcule a folha para que o sistema considere a configuração atualizada de feriados. 

### Data de apuração do ponto inadequada

A data de apuração do ponto define qual período será considerado para o cálculo do DSR. Se esta data estiver configurada incorretamente, o sistema pode considerar dias úteis e não úteis de forma equivocada, resultando em valores incorretos.

**Solução:**

**(1)** Acesse a tela **"Empresas"** (Configurações » Cadastros » Pessoal » Empresas). 

**(2)** Localize o campo **"Dia de Apuração do Ponto"** e verifique se está configurado corretamente conforme a política da empresa.

![Imagem 1: (1) Acesse a tela "Empresas" ( Configurações » Cadastros » Pessoal » Empresas ). (2) Localize o campo "Dia de Apuração…](https://ajuda.sankhya.com.br/hc/article_attachments/41262820179095)

**(3)** Ajuste a data de apuração, se necessário, para o dia correto. 

**(4)** Recalcule a folha para que o sistema aplique o período correto de apuração. 

### Fórmula personalizada de DSR

Algumas empresas utilizam fórmulas personalizadas para o cálculo do DSR, especialmente quando há particularidades como período de apuração diferenciado ou cálculo sobre comissões. Se a fórmula estiver inadequada, o valor calculado pode não corresponder ao esperado.

**Solução:**

**(1)** Acesse a tela **"Eventos"** (Pessoal+ » Cadastros » Eventos) e localize o evento de DSR utilizado. 

**(2)** Verifique a fórmula de cálculo configurada e analise se as variáveis estão corretas (dias úteis trabalhados, dias não úteis, valores de horas extras, etc.). 

**(3)** Se necessário, entre em contato com a equipe de implantação para revisar e ajustar a fórmula conforme as necessidades da empresa. 

**(4)** Após o ajuste, recalcule a folha para validar o novo cálculo. 

### DSR em rescisões com poucos dias trabalhados

Em casos de rescisão onde o colaborador trabalhou poucos dias no mês, o cálculo do DSR pode resultar em valores que parecem duplicados ou iguais ao valor das horas extras. Isso ocorre porque a fórmula divide o valor das verbas pelos dias úteis trabalhados e multiplica pelos dias não úteis.

Por exemplo, se um colaborador teve seu contrato encerrado no dia 02/01, ele trabalhou apenas 1 dia útil e teve 1 dia não útil. A fórmula fica: Valor da Hora Extra ÷ 1 × 1 = Valor da Hora Extra, resultando no mesmo valor.

Este comportamento está correto conforme a fórmula padrão do sistema. Se a empresa discordar deste cálculo, é necessário revisar a fórmula com a equipe de implantação.
