---
id: "42427230315031"
titulo: "Como configurar uma cerca virtual para restringir o registro de ponto no local de trabalho"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427230315031-Como-configurar-uma-cerca-virtual-para-restringir-o-registro-de-ponto-no-local-de-trabalho"
trilha: "PONTOTEL: Sistema de marcação de ponto > Gestão"
atualizado_em: "2026-08-03T13:29:56Z"
rotulos: ["sync_hc", "pontotel_6a332851bc1d9d4e54cdc545", "sync_hash_8352f3516aac", "pontotel"]
---

# Como configurar uma cerca virtual para restringir o registro de ponto no local de trabalho

A cerca virtual permite **limitar o registro de ponto a um raio específico do local de trabalho**. Essa configuração garante maior controle e precisão dos registros, evitando marcações feitas fora do local definido.

Se a cerca virtual estiver ativa e o colaborador tentar registrar o ponto fora do endereço do local de trabalho vinculado ao seu cadastro, o sistema bloqueará o registro de ponto e exibirá uma notificação informando que ele se encontra fora da área permitida.

Esse processo segue as diretrizes estabelecidas pela legislação vigente, incluindo a Portaria nº 671 do Ministério do Trabalho.
Veja abaixo como fazer a configuração completa da cerca virtual para registro no app BatePonto.

---

## Passo 1: Adicione o endereço no local de trabalho

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros**, depois selecione a opção **Locais de trabalho**.
2. Selecione e edite o local desejado, ou crie um novo local de trabalho. No cadastro do local, preencha o **endereço** no campo acima do mapa, conforme indicado na imagem abaixo.

   ![Imagem 1: Selecione e edite o local desejado, ou crie um novo local de trabalho. No cadastro do local, preencha o endereço no…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_pbhzf9.png)
3. Ao digitar o endereço, uma lista suspensa será exibida com sugestões baseadas na base de dados. Selecione o endereço correto para que os campos adicionais sejam preenchidos automaticamente.
4. No campo correspondente, preencha o número do endereço.

   ![Imagem 2: No campo correspondente, preencha o número do endereço.](https://storage.crisp.chat/users/helpdesk/website/-/5/3/3/e/533e139f08befc00/7b529213-5f6d-450e-abf1-a616e8_m8yugm.png)
5. Abaixo do mapa, você pode definir a distância máxima da [cerca virtual](https://sankhya.zendesk.com/hc/pt-br/articles/42427230315031) em metros. Quando preenchido, esse valor terá prioridade e substituirá a distância configurada no [perfil de coletor](https://sankhya.zendesk.com/hc/pt-br/articles/42427310963095). Caso esse campo seja deixado em branco, será considerada a distância definida no perfil de coletor.

![Imagem 3: Abaixo do mapa, você pode definir a distância máxima da cerca virtual em metros. Quando preenchido, esse valor terá…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_6v1bkt.png)
> 💡 Dica: Se o PIN no mapa não estiver posicionado exatamente sobre o local de trabalho, clique e arraste-o até a localização correta para garantir maior precisão.

---

## Passo 2: Ajuste o cadastro do empregado

1. No menu de navegação do [site Gestão](https://gestao.pontotel.com.br/), clique em **Cadastros**, e selecione a opção **Empregados**.
2. Abra o cadastro do empregado, na seção "**config. de ponto e benefícios**".

   ![Imagem 4: Abra o cadastro do empregado, na seção " config. de ponto e benefícios ".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1wyq259.png)
3. **Desative** a opção "**registra ponto em qualquer local de trabalho**", para que os pontos deste colaborador fiquem limitados somente ao local de trabalho do seu cadastro.

   ![Imagem 5: Desative a opção " registra ponto em qualquer local de trabalho ", para que os pontos deste colaborador fiquem…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_113dceg.png)
4. **Ative** a opção "**mostrar feedback no aplicativo**", para que o colaborador veja o motivo do bloqueio no app.

   ![Imagem 6: Ative a opção " mostrar feedback no aplicativo ", para que o colaborador veja o motivo do bloqueio no app.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_1kv6p19.png)
5. **[Opcional]** Caso possua o módulo **Redução de Riscos no Registro**, é possível definir em quais momentos a cerca virtual será obrigatória.

   - Por exemplo: exigir a validação apenas nos registros de Entrada e Saída, permitindo que a Pausa e o Retorno da Pausa sejam realizadas de qualquer local. Para isso, basta selecionar os momentos em que a cerca virtual deverá ser aplicada.

   ![Imagem 7: Por exemplo: exigir a validação apenas nos registros de Entrada e Saída, permitindo que a Pausa e o Retorno da Pausa…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_19qq8ue.png)

---

## Passo 3: Configure o perfil de coletor do App BatePonto

1. No menu, clique em **Gestão**, depois selecione a opção **Coletores**.

   [GIF animado: Imagem 8: No menu, clique em Gestão , depois selecione a opção Coletores .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/gestao-coletores_1324wt0.gif)
2. Na nova tela, mude para a seção **perfil de coletores**, depois troque a categoria para "**aplicativo de registro**" (que se refere às configurações do App BatePonto). Em seguida, selecione o perfil de coletor desejado, e clique no ícone de lápis para **editar** o perfil.

![Imagem 9: Na nova tela, mude para a seção perfil de coletores , depois troque a categoria para " aplicativo de registro " (que se…](https://storage.crisp.chat/users/helpdesk/website/-/a/8/a/4/a8a4ac02fc485000/429f7eb3-989a-44ab-890e-69dd53_s8s1u3.png)
> ⚠️ Atenção: Caso possua apenas um perfil, ele será utilizado por todos os aplicativos BatePonto cadastrados. Se precisar aplicar restrições apenas a alguns aplicativos, crie um novo perfil de coletor clicando em **criar novo perfil de coletor** e configure-o conforme explicado abaixo.

3. Na seção "opções de localização", selecione a opção "**ativar localização**".

![Imagem 10: Na seção "opções de localização", selecione a opção " ativar localização ".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_jg348n.png)
> 💡 Dica: Recomendamos ativar também a opção “detectar manipulação”, para que o aplicativo consiga identificar possíveis alterações nas coordenadas geográficas do dispositivo, como o uso de VPN, GPS falso ou outros recursos de simulação de localização.

4. Defina o **raio de distância** permitido para o registro de ponto a partir do endereço do local de trabalho.

   ![Imagem 11: Defina o raio de distância permitido para o registro de ponto a partir do endereço do local de trabalho.](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ur385j.png)
5. Na seção "opções de governança", **desative** a opção "**permitir marcação longe do local de trabalho**".

![Imagem 12: Na seção "opções de governança", desative a opção " permitir marcação longe do local de trabalho ".](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_ex5wup.png)

---

## Passo 4: Ajuste os coletores já existentes que deseja aplicar a cerca virtual

1. No menu, clique em **Gestão**, depois selecione a opção **Coletores**.
2. Dessa vez, em "gestão de coletores", fique na seção **coletores**, e troque a categoria para **aplicativo de registro** (referente às configurações do App BatePonto).

   ![Imagem 13: Dessa vez, em "gestão de coletores", fique na seção coletores , e troque a categoria para aplicativo de registro…](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6762c4dc42050c172896a867/file-queQwMBIeR.png)
3. Na lista de coletores, selecione o coletor desejado e clique em **editar.**

   ![Imagem 14: Na lista de coletores, selecione o coletor desejado e clique em editar.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6762c51b2ac49b2480e16c11/file-G4ZYu5m96k.png)
4. Altere o perfil do coletor para aquele que possui a restrição configurada.

   ![Imagem 15: Altere o perfil do coletor para aquele que possui a restrição configurada.](https://d33v4339jhl8k0.cloudfront.net/docs/assets/574ca4e4c6979138ff609a77/images/6762c541a6e97169ffc0ea06/file-bjXIJXas5U.png)
5. Caso tenha editado o perfil existente, apenas confirme se o coletor está vinculado corretamente a esse perfil.

---

> ⚠️ Atenção:

- A restrição por localização se aplica somente aos registros feitos pelo aplicativo **BatePonto**. Registros realizados pelo BatePonto Web (computador) ou pelo Aplicativo Pontotel Gestão não possuem essa restrição.
- A validação por geolocalização depende do **GPS do aparelho do colaborador**. A Pontotel **não é um GPS** nem ativa o GPS sozinho. É feita somente a **leitura das coordenadas que o próprio dispositivo fornece** no momento do registro. Se a localização estiver desativada, com permissão negada ou imprecisa, a cerca virtual não poderá ser validada e o ponto poderá ser bloqueado ou marcado fora da área. Oriente os colaboradores a manter o **GPS ligado** e a conceder a permissão de **Localização** ao app (Android/iOS: Ajustes/Configurações → Aplicativos → Pontotel → Localização → “Permitir ao usar o app” ou “Sempre”).

---

Com essa configuração, você garante que os registros de ponto sejam realizados apenas dentro do local definido, proporcionando maior controle e segurança nos apontamentos.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
