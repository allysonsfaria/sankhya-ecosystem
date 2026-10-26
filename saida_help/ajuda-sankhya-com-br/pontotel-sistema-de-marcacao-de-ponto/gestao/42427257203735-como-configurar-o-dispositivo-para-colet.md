---
id: "42427257203735"
titulo: "Como configurar o dispositivo para coletar a localização do registro de ponto"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427257203735-Como-configurar-o-dispositivo-para-coletar-a-localiza%C3%A7%C3%A3o-do-registro-de-ponto"
trilha: "PONTOTEL: Sistema de marcação de ponto > Gestão"
atualizado_em: "2026-10-06T17:02:49Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3328e6d2d5419b8613e82b", "sync_hash_000ab0481ec7"]
---

# Como configurar o dispositivo para coletar a localização do registro de ponto

Os aplicativos BatePonto e Pontotel Gestão permitem que colaboradores registrem seus pontos mesmo sem conexão com a internet, por meio do modo **offline**. Nesse caso, as marcações ficam armazenadas no dispositivo e são sincronizadas automaticamente quando houver conexão disponível.
Uma dúvida comum é se os pontos registrados offline gravam a **localização**. Sim, a localização pode ser registrada, desde que o dispositivo esteja com o **GPS ativo** e as permissões necessárias concedidas no momento da marcação. Além disso, para evitar inconsistências, é importante que o **fuso horário automático** do smartphone esteja ativado, pois o sistema possui mecanismos antifraude relacionados à hora do aparelho.

Neste artigo, você vai aprender o que precisa ser ativado no celular para que a localização seja registrada corretamente, mesmo em pontos feitos offline.

---

## Como configurar o celular

1. **Atualize o aplicativo**

   - Certifique-se de que está utilizando a versão mais recente do app.
   - Acesse a loja de aplicativos correspondente ao aparelho, e verifique se há uma atualização disponível para o app. Caso ainda não tenha o aplicativo instalado, faça o download.

   [App BatePonto | Android](https://play.google.com/store/apps/details?id=com.pontotel.bateponto&hl=pt_BR)
   [App BatePonto | IOS (Iphone)](https://apps.apple.com/br/app/bateponto-controle-de-ponto/id1531898009)

   [App Pontotel Gestão | Android](https://play.google.com/store/apps/details?id=com.pontotel.appgestor&hl=pt_BR)
   [App Pontotel Gestão | IOS (Iphone)](https://apps.apple.com/br/app/pontotel-gest%C3%A3o/id1457844741)
2. **Conceda permissões ao app**

   - Na primeira vez que abrir o aplicativo, autorize o uso de **localização, câmera e armazenamento**.
   - Caso já tenha o app instalado, vá nas configurações do aplicativo e ative todas as permissões.

   ![No Iphone, por exemplo, é possível verificar as permissões do app acessando: Ajustes > Apps](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/app-iphone_n8lh48.jpg)

   No Iphone, por exemplo, é possível verificar as permissões do app acessando: Ajustes > Apps

> 💡 Dica: Cada smartphone possui um caminho diferente para acessar as configurações do app. Se não sabe como acessá-las, pesquise no Google: "Como acessar as configurações de aplicativo no smartphone [marca] e [modelo]".

3. **Ative os serviços de localização (GPS)**

   - Ainda nas configurações do aparelho, procure a opção de **localização**ou **GPS**e ative. Caso não encontre, faça uma pesquisa no Google, conforme orientado na dica acima.
   - Sem essa ativação, o app não conseguirá registrar coordenadas.
4. **Ative o fuso horário automático**

   - Agora busque nas configurações do aparelho o ajuste de**data e hora**. Nessa opção, habilite a opção **Fuso horário automático**.
   - Isso evita bloqueios no registro offline e garante que os horários sejam validados corretamente pelo sistema.
5. **Aguarde a captura do GPS antes de registrar o ponto**

   - Em locais abertos ou próximos a janelas, aguarde alguns segundos para que o celular capture a posição com mais precisão.
6. **Registre o ponto normalmente**

   - No aplicativo, toque em **Bater ponto** e confirme.
   - O app salva o ponto localmente e, se o GPS estiver ativo, registra também as coordenadas.
7. **Sincronize os pontos**

   - Assim que houver internet disponível, abra o app e permita que ele sincronize. Essa sincronização é feita de forma automática, mas também é possível fazer uma sincronização manual no app BatePonto. Para saber como fazer, veja este [artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427333327511).
   - Isso garante que o ponto, a foto e a localização sejam enviados para o sistema.

---

> ⚠️ Atenção:

- **Ponto offline com localização**: o app registra a localização apenas se o **GPS estiver ativo** e o app tiver permissão. Caso contrário, o ponto será salvo sem coordenadas.
- **Coleta de dados:** Os aplicativos da Pontotel fazem apenas a **coletados dados de localização** do dispositivo utilizado para o registro de ponto.
- **Fuso horário automático**: manter essa configuração ligada no celular é obrigatório para que o sistema valide corretamente os registros.
- **Precisão da localização**: em locais fechados ou sem sinal de GPS, a precisão pode ser menor. Oriente os colaboradores a registrar o ponto em locais com sinal melhor.
- **Sincronização diária**: é fundamental que os colaboradores sincronizem o aplicativo todos os dias para evitar atrasos e falhas no envio das informações.
- **Configuração do perfil de coletor:** Para que o coletor faça a captura da localização, também é necessário que a opção "ativar localização" esteja habilitada no perfil de coletor. Para saber mais sobre perfil de coletor, consulte este [artigo](https://sankhya.zendesk.com/hc/pt-br/articles/42427310963095). Caso não tenha a permissão necessária para fazer ajustes no sistema, consulte o RH da sua empresa.

![Opção que deve estar ativada no perfil de coletor](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_14p70x9.png)

Opção que deve estar ativada no perfil de coletor

---

O registro offline dos aplicativos BatePonto garante que os colaboradores possam registrar suas jornadas mesmo sem internet, mas para que a **localização seja registrada corretamente**, é essencial que o celular tenha o **GPS ativo**, o **fuso horário automático ligado** e que o app tenha todas as permissões concedidas. Além disso, a sincronização diária assegura que todos os pontos sejam enviados ao sistema sem perdas.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0).
