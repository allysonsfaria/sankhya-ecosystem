---
id: "10632759838743"
titulo: "Campo de preenchimento obrigatório - Indicativo de tipo de apuração de IR"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/10632759838743-Campo-de-preenchimento-obrigat%C3%B3rio-Indicativo-de-tipo-de-apura%C3%A7%C3%A3o-de-IR"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:16:31Z"
rotulos: ["Configuração", "eSocial", "Folha de Pagamento", "#folha", "Campo obrigatório - tipo de apuração de IR", "Erro ao enviar evento S-2299 eSocial", "Preencher \"Incidência p/ IRRF\" conforme Tabela 21 do eSocial e reenviar o evento", "Erro", "IRRF", "Artigo atualizado KCS", "Sankhya RH - KCS"]
---

# Campo de preenchimento obrigatório - Indicativo de tipo de apuração de IR

O campo "Incidência p/ IRRF" da aba eSocial deve estar preenchido, quando houver incidência de IRRF para o cálculo. (Mensagem de erro: Campo de preenchimento obrigatório - Indicativo de tipo de apuração de IR).

### SITUAÇÃO

Esta mensagem aparece ao tentar salvar a configuração de eventos de folha de pagamento quando há inconsistência entre as configurações da aba **"Avançado"** (onde a incidência de IRRF está marcada) e da aba **"eSocial"** (onde o campo **"Incidência p/ IRRF"** está vazio ou incorreto).

### SOLUÇÃO

Para corrigir o erro, ajuste a configuração do evento seguindo os passos abaixo:

**(1)** Acesse a tela **"Cadastro de Eventos"** (Pessoal >> Cadastros >> Eventos) e localize o evento que está apresentando o erro.

**(2)** Abra o evento e acesse a aba **"Avançado"**. Verifique se a opção **"IRRF"** está marcada para incidir.

![Imagem 1: Acesse a aba "eSocial" e localize o campo "Incidência p/ IRRF" .](https://ajuda.sankhya.com.br/hc/article_attachments/41065080936215)

**(3)** Acesse a aba **"eSocial"** e localize o campo **"Incidência p/ IRRF"**.

![Imagem 2: Preencha o campo "Incidência p/ IRRF" com o código correto conforme a Tabela 21 do eSocial (Tabela S-1010). Para…](https://ajuda.sankhya.com.br/hc/article_attachments/41065080936855)

**(4)** Preencha o campo **"Incidência p/ IRRF"** com o código correto conforme a Tabela 21 do eSocial (Tabela S-1010). Para eventos personalizados, utilize os códigos apropriados. 

**(5)** Salve as alterações realizadas no evento.

**(6)** Envie o evento **S-1010** (Tabela de Rubricas) da rubrica alterada. Se o evento já foi transmitido anteriormente, será necessário retificar o **S-1010** com validade retroativa sempre que houver ajuste na aba e-social.

**Observação importante:** Eventos padrões do sistema possuem configurações automáticas. Para eventos personalizados, é fundamental realizar a configuração manual correta em ambas as abas para garantir a consistência dos valores enviados ao e-social com o valores apresentado no resumo de folha.

### CAUSA

O erro ocorre devido à inconsistência entre as configurações das abas **"Avançado"** e **"eSocial"**. Quando o campo **"IRRF"** está marcado para incidir na aba **"Avançado"**, o sistema exige que o campo **"Incidência p/ IRRF"** na aba **"eSocial"** esteja preenchido com um código válido da tabela oficial do eSocial. A ausência ou erro neste preenchimento impede a validação do envio das informações fiscais.
