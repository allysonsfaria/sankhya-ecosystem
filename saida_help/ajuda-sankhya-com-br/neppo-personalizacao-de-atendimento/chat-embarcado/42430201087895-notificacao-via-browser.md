---
id: "42430201087895"
titulo: "Notificação via browser"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430201087895-Notifica%C3%A7%C3%A3o-via-browser"
trilha: "NEPPO: Personalização de atendimento > Chat Embarcado"
atualizado_em: "2026-08-11T16:58:54Z"
rotulos: ["sync_hc", "neppo", "neppo_421330960", "sync_hash_80d1bf5dd8cd"]
---

# Notificação via browser

As notificações via browser funcionam da seguinte forma:

- Temos uma função que abre o chat e seleciona a sessão da mensagem

- Essa função está sendo enviada como um callback no evento '`neppo-browser-focus`'

- Devido a restrições de permissão e segurança de browser (google chrome), uma parte do código deve ser executada diretamente no site que hospeda o chat embarcado, sendo esta parte a que coleta a permissão do usuário final para o disparo de notificações e também o clique na notificação fazer abrir o chat.

- Dentro do evento irá chegar:

- callback: função implementada na plataforma Neppo que abre o chat e abre a sessão da mensagem
- sessionObj: Objeto contendo informações da sessão
- logoUrl: url da imagem do logo
- messagePart: parte da mensagem

- O evento será acompanhado das notificações sonoras e também enquanto o usuário estiver em outra aba

- Segue a proposta de como o cliente que hospeda deverá implementar o código

## Testes feitos no Angular 14.2.0

```
      <div [style.display]="loading ? 'none' : 'block'"
           style="height: 500px; width: 100%;">
        <iframe [srcdoc]="iframeHtml"
                allow="notifications"
                sandbox="allow-same-origin allow-scripts allow-forms allow-popups allow-downloads"
                (load)="onLoadIframe($event)">
        </iframe>
      </div>
```

```
onLoadIframe(ev: Event) {
    const iframe = ev.target as HTMLIFrameElement;

    // Adicionar o evento criado
    iframe.contentWindow?.addEventListener(
      'neppo-browser-focus',
      (customEvent: any) => {
        const sessionObj = customEvent.detail.sessionObj;
        const user = sessionObj?.user;

        const logoUrl = customEvent.detail.logoUrl;,
        const messagePart = customEvent.detail.messagePart;

        let body = 'Nova mensagem';

        if ('Notification' in window) {
          Notification.requestPermission().then((permission) => {
            const displayName = user?.displayName;
            const userPhone = user?.phone;

            body = `${userPhone ? `${userPhone}` : ''}: ${messagePart}`;

            const titleNotification = `${displayName ?? 'Notificação'}`;

            if (permission === 'granted') {
              const notificationBrowser = new Notification(titleNotification, {
                body,
                icon: logoUrl,
              });

              notificationBrowser.onclick = () => {
                // chama o callback implementado na plataforma Neppo
                customEvent.detail.callback();
                window.focus();
              };
            }
          });
        }
      }
    );
  }
```
