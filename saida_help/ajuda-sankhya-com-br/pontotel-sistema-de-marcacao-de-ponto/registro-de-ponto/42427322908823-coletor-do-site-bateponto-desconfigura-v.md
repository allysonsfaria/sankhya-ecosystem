---
id: "42427322908823"
titulo: "Coletor do site BatePonto desconfigura? Veja uma solução com a configuração de Cookies"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427322908823-Coletor-do-site-BatePonto-desconfigura-Veja-uma-solu%C3%A7%C3%A3o-com-a-configura%C3%A7%C3%A3o-de-Cookies"
trilha: "PONTOTEL: Sistema de marcação de ponto > Registro de Ponto"
atualizado_em: "2026-08-03T12:52:53Z"
rotulos: ["sync_hc", "pontotel", "pontotel_6a3329e4a7a6db7e7f9413a6", "sync_hash_307d827e6b3d"]
---

# Coletor do site BatePonto desconfigura? Veja uma solução com a configuração de Cookies

Você já configurou um computador para registrar o ponto na sua empresa ([BatePonto Web](https://bateponto.pontotel.com.br/#/marcacao)), mas, passado algum tempo, ele pediu login e senha novamente, como se nunca tivesse sido cadastrado?
Isso acontece por uma medida de segurança do seu **navegador** (Google Chrome, Edge, etc.).

Para atender às exigências da **Portaria 671** e garantir que o ponto está sendo registrado no dispositivo correto, o BatePonto salva um arquivo de identificação no seu navegador, chamado **Cookie**.
Se o seu navegador estiver configurado para **"Limpar cookies ao fechar"** ou se você usar uma **Guia Anônima**, esse arquivo é apagado ao fechar a janela. Resultado: o sistema "esquece" que aquele computador é um coletor autorizado.

---

## Como resolver? (Configurando o Google Chrome)

Para evitar que o BatePonto desconecte sozinho, você precisa permitir que o site da Pontotel salve os dados no seu navegador.
Veja como configurar no **Google Chrome**:

1. Abra o navegador Chrome e, no canto superior direito, clique nos **três pontinhos** e selecione **Configurações**.

   [GIF animado: Imagem 1: Abra o navegador Chrome e, no canto superior direito, clique nos três pontinhos e selecione Configurações .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/config-chrome_dncpx0.gif)
2. No menu lateral esquerdo, clique em **Privacidade e segurança** e depois em "**Cookies de terceiros"** (ou **"Cookies e outros dados do site"**).

   ![Imagem 2: No menu lateral esquerdo, clique em Privacidade e segurança e depois em " Cookies de terceiros" (ou "Cookies e outros…](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_14wxdxz.png)
3. Clique no botão **Adicionar** ao lado de "Sites que podem usar cookies sempre".
4. Na janela que abrir, digite o seguinte endereço: `[*.]pontotel.com.br`
5. Marque a caixinha **"Incluir cookies de terceiros neste site"** (se houver) e clique em **Adicionar**.

![Imagem 3: Marque a caixinha "Incluir cookies de terceiros neste site" (se houver) e clique em Adicionar .](https://storage.crisp.chat/users/helpdesk/website/-/c/e/8/7/ce87d16ae4000000/image_6icf3u.png)

---

> ⚠️ Atenção: Se você utiliza o BatePonto em Guia Anônima ou Modo Privado, o coletor sempre será descadastrado ao fechar a janela. Isso é o comportamento padrão da navegação anônima (não salvar dados). Para um coletor de ponto fixo, recomendamos **não utilizar** o modo anônimo, ou você terá que realizar o login e configuração do coletor todos os dias.

---

Com essa configuração simples, você garante que o Chrome mantenha as informações do [BatePonto](https://bateponto.pontotel.com.br/#/marcacao) salvas, evitando o retrabalho de configurar o coletor.

Caso ainda tenha dúvidas ou precise de auxílio, entre em contato com o nosso time de Suporte pelo chat integrado ao [site Pontotel Gestão](https://gestao.pontotel.com.br/#/cognito/login) ou pelo [WhatsApp](https://api.whatsapp.com/send/?phone=551131852700&text&type=phone_number&app_absent=0)!
