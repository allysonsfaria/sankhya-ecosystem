---
id: "42427523241879"
titulo: "Como realizar o Check-in Verificado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427523241879-Como-realizar-o-Check-in-Verificado"
trilha: "PLOOMES: Automação de propostas  > Aplicativo Ploomes (Mobile)"
atualizado_em: "2026-08-11T16:14:30Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5754489", "sync_hash_ef2ad956a890"]
---

# Como realizar o Check-in Verificado

O recurso de **Check-in/Check-out** permite registrar visitas realizadas em campo, garantindo mais controle, rastreabilidade e precisão nas informações registradas pelos usuários.

## Para que serve?

O Check-in/Check-out possibilita que o usuário:

- Registre o **início da visita** (check-in);
- Finalize a visita com **check-out** (quando habilitado);
- Tenha suas visitas verificadas por **coordenadas de GPS**, validando a presença no local.

É ideal para equipes externas, acompanhamento de rotinas de campo e gestão de produtividade.

## Pré-requisitos

Antes de utilizar o recurso, verifique:

1. **Permissão de localização** concedida ao app Ploomes;
2. **Localização precisa** ativada no dispositivo;
3. **GPS ligado**;
4. Configuração da conta em **Administração → Módulos do Sistema → Tarefas**, onde é possível:

   - Ativar/desativar Check-out;
   - Definir o tamanho do raio de verificação do check-in e check-out em metros (é a distância máxima do endereço para validar o check-in/check-out).

![Imagem 1: Definir o tamanho do raio de verificação do check-in e check-out em metros (é a distância máxima do endereço para…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223991497/aed5f21c1634fdce05edd94d01db/image.png?expires=1786536000&signature=3152de82cc39fbb3ac01c1e36aa2e4a54d3de2d53bf6119bf59832c75432ddc0&req=dSIlFcB3nIVWXvMW3nq%2Bga95%2BJuX9AIw2eeh6mRWy7aXWVetl4aj6m4EHQRY%0ADSwFyFzgwh%2FCvcX2alqmQyuFhvA%3D%0A)

Além disso, o Ploomes valida o check-in usando o endereço da tarefa ou do cliente. Isso pode gerar as situações abaixo:

- O cliente **possui endereço válido** → check-in verificado com raio exibido no mapa;
- O cliente **não tem endereço** → check-in não verificado (sem raio);
- O endereço **não é reconhecido pelo Google Maps** → sem coordenadas → check-in não verificado;
- O usuário está em local **sem endereço** (ex.: área rural) → coordenadas são coletadas, mas pode resultar em check-in não verificado.

![Imagem 2: O usuário está em local sem endereço (ex.: área rural) → coordenadas são coletadas, mas pode resultar em check-in não…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223991816/771ca1b94e44e72c74729f91f2e4/image+%281%29.png?expires=1786536000&signature=821186290a331683f73f3de718cea938c70d0c484906a76ae3b732ce22050f13&req=dSIlFcB3nIleX%2FMW3nq%2Bgfkr3C8G3akpXnvcEhCIsvBEh4PyDGiuNMm1%2Fqkq%0AA4PUWA5nID7wY4kvElRJs%2FgxXps%3D%0A)

## Check-in/Check-out em Tarefas

## Como iniciar o Check-in

1. Acesse a tarefa desejada;
2. Toque no botão flutuante **“Iniciar Check-in”** no canto inferior direito;
3. No modal de check-in, você verá:

   - Se você está **dentro ou fora do raio** do endereço (círculo verde);
   - Sua localização no mapa (pin com foto);
   - Localização do endereço da tarefa (pin vermelho);
   - Ícone de mapa para abrir rota no app de navegação.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=RqjSvRoWHu0)

## Check-in em andamento

Na tela de **Registro da Visita**, é possível:

- Fazer anotações;
- Acompanhar o tempo em visita;
- Ver sua localização atual no mapa.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=IU0XMg1aQag)

O registro pode ser **minimizado** para permitir navegação no aplicativo (ou até fora dele) sem encerrar a visita.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=k7zxdwC4_Y0)

### Cancelar ou deletar o registro

Toque nos **três pontos** (⋮) para:

- Cancelar os dados do check-in;
- Deletar o registro da visita.

![Imagem 3: Deletar o registro da visita.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223993582/c8ab6d7aa3bbf49106207658dbee/image+%282%29.png?expires=1786536000&signature=c5e6fba26718b05e0c906313ce0a8b81af6ac646194a26401c0f680499d6e9a2&req=dSIlFcB3noRXW%2FMW3nq%2BgVgSxhfR96k0JsC3%2FJ74mnd705W3lCDcK%2BQDdxYx%0A9mIyQaCtzL9R9PA53hgkSbYCiUQ%3D%0A)

## Realizar Check-out

Ao finalizar a visita:

1. Selecione **“Realizar Check-out”**;
2. A visita é encerrada e a tarefa finalizada;
3. O Registro da Visita é salvo automaticamente.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=3FZCAvVSF3s)

Para consultar depois, acesse **Atividades**, o **histórico do cliente** ou o **histórico do negócio** e abra o registro desejado. Você pode navegar pelas informações e editar informações clicando em "Editar" (exceto dados de localização de Check-in/Check-out e duração da visita).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=QVrgpT9a1YM)

## Check-in/Check-out em Registro de Interação

## Como iniciar o check-in

1. Toque no botão flutuante de criar registro (em Atividades, Cliente ou Negócio);
2. Escolha **Registro de Interação**;
3. Selecione o tipo **Visita** e preencha o cliente;
4. Toque em **“Iniciar Check-in”**.

![Imagem 4: Toque em “Iniciar Check-in” .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223994009/592536c2656293fbfeaec6751da3/image+%283%29.png?expires=1786536000&signature=ece2f9ee0d8500b40462e9935216c291781d7e529fda51c74ea0ced9ed3f07de&req=dSIlFcB3mYFfUPMW3nq%2BgW%2BN6sXFw3OXGTUL7ljDJiRqBl9xwkGCUjf60047%0A7Ch4Axu2RxspiKfaAM7OsQwvDoQ%3D%0A)

![Imagem 5: Toque em “Iniciar Check-in” .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223994328/6429a9580cd6f4401a6181f41deb/image+%284%29.png?expires=1786536000&signature=2ccbd99ada20a52734fca185264506790e608170042d8ab05a62842152ee4e7d&req=dSIlFcB3mYJdUfMW3nq%2BgUFy%2BG26x5dW3fKBF4k%2B8zLkXM7udE1maTiY1ILS%0Ap07SgOEOqABSTpncKHiErkiTp%2Bs%3D%0A)

![Imagem 6: Toque em “Iniciar Check-in” .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223994813/3de5dc19724a53d157059d4b26ba/image+%285%29.png?expires=1786536000&signature=386a748e3b800a5f60b6d412d55b0d5dcf02109a426a0c7ffd6950ad73a26e75&req=dSIlFcB3mYleWvMW3nq%2BgQjdrg1zcEynVVxGWk1YhjIbF%2BWN3D3WRdVKYgf%2B%0AyJsHxN9K8AvWJ6uUHZUm46gOc9I%3D%0A)

Ao iniciar o Check-in, o modal 'some' e você é direcionado para a tela de Registro da Visita. Na tela de Registro da Visita é possível:

- Minimizar o registro;
- Cancelar dados;
- Deletar o registro;
- Realizar check-out.

![Imagem 7: Realizar check-out.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223995137/b4052342aef38d94218d350ec5ce/image+%287%29.png?expires=1786536000&signature=336e9dab2043ed9efe5d36482b132c57c94ae0bf500e18f2ffe49c579707a3b8&req=dSIlFcB3mIBcXvMW3nq%2BgVXEkkqcZhrQLXeMO%2B%2Foe%2BWcO8z%2BeE6qWX3alYxO%0A0S5I6zx94KR0YGfmaOwkDUD2jXE%3D%0A)

## Realizar Check-out

Ao finalizar a visita:

1. Selecione **“Realizar Check-out”**;
2. A visita é encerrada e a tarefa finalizada;
3. O Registro da Visita é salvo automaticamente.

Para consultar depois, acesse **Atividades**, o **histórico do cliente** ou o **histórico do negócio** e abra o registro desejado. Você pode navegar pelas informações e editar informações clicando em "Editar" (exceto dados de localização de Check-in/Check-out e duração da visita).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=eXFoQMH3G74)

## Check-in/Check-out pelo menu "Check-in de visitas"

## Como iniciar o check-in

1. Toque no botão flutuante → **Check-in de visitas**;
2. O modal de início será exibido;
3. Confirme **“Iniciar Check-in”**;
4. Você será direcionado ao Registro da Visita.

![Imagem 8: Você será direcionado ao Registro da Visita.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1223995936/9af1a6ac31a29e12ebab20cf36cf/image+%288%29.png?expires=1786536000&signature=26af3d228a9f9c1618f1a7eb1214b4fa703579c1fcdf6a536348ffc38b2338b2&req=dSIlFcB3mIhcX%2FMW3nq%2Bgc06ZxF9hr9qzOi3TFXiO%2FEC6ox1Vlw0azhTBHm0%0AXIaCfBuMgeYRs9n3FCx4iHryC38%3D%0A)

Ao iniciar o Check-in, o modal some e você é direcionado para a tela de Registro da Visita. Na tela de Registro da Visita é possível:

- Minimizar o registro;
- Cancelar dados;
- Deletar o registro;
- Realizar check-out.

## Realizar Check-out

Ao finalizar a visita:

1. Selecione **“Realizar Check-out”**;
2. A visita é encerrada e a tarefa finalizada;
3. O Registro da Visita é salvo automaticamente.

Para consultar depois, acesse **Atividades**, o **histórico do cliente** ou o **histórico do negócio** e abra o registro desejado. Você pode navegar pelas informações e editar informações clicando em "Editar" (exceto dados de localização de Check-in/Check-out e duração da visita).

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=6u3m1f6tduI)

## Quando a conta utiliza somente Check-in

Se o Check-out estiver desativado na conta:

- O usuário registra **apenas o Check-in**;
- Não há contabilização de duração da visita.

O fluxo é idêntico aos anteriores, mas finaliza pressionando o **check (✔️)** no Registro da Visita.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=LYQkam7izEw)

## Somente Check-in em Registro de Interação

1. Toque no botão flutuante de criação de registro (Atividades, Cliente ou Negócio) e selecione **Registro de Interação**;
2. Escolha o tipo **Visita** e preencha o formulário;
3. Toque em **“Realizar Check-in”**, confira o cliente e endereço, e confirme;
4. Navegue normalmente na tela de Registro da Visita;
5. Finalize a visita tocando no **check (✔️)**.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=JVKa8BwptRc)

## Somente Check-in em Check-in de Visitas

1. Toque no botão flutuante de criação de registro e selecione **Check-in de visitas**;
2. Escolha o cliente;
3. Toque em **“Realizar Check-in”**;
4. Navegue normalmente na tela de Registro da Visita;
5. Finalize tocando no **check (✔️)**.

[Vídeo: tutorial do artigo](https://www.youtube.com/watch?v=VWgyhc42jAI)

## Como identificar Check-ins Verificados em filtros, relatórios e metas

Um **check-in verificado** apresenta os seguintes campos preenchidos no Registro de Interação:

Para check-in:

- **Check-in verificado**: é preenchido com "Sim"
- **Data de CheckIn**
- **Endereco de CheckIn**
- **Latitude de CheckIn**
- **Longitude de CheckIn**

Para check-out:

- **Verificacao de CheckOut**: é preenchido com "Sim"
- **Data de CheckOut**
- **Endereco de CheckOut**
- **Latitude de CheckOut**
- **Longitude de CheckOut**

💡 Dica: use "Check-in verificado" - igual a - "Sim" em filtros.

Veja também:

[Como criar relatórios](https://sankhya.zendesk.com/hc/pt-br/articles/42427389079447)

[Funcionamento de abas e filtros](https://sankhya.zendesk.com/hc/pt-br/articles/42427527818903#como-fazer)

[Como criar metas](https://sankhya.zendesk.com/hc/pt-br/articles/42427513869591)

---

## Acesse a Universidade Ploomes para saber mais

A Ploomes disponibiliza uma plataforma de educação digital criada para capacitar seus clientes, oferecendo uma variedade de cursos, shorts e casos de uso.

Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.

[![Imagem 9: Abaixo, você confere sugestões de conteúdos disponíveis em nossa plataforma que se relacionam ao tema deste artigo.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/1243759765/69b66e50c873ca0a13c61217cc83/Intercom+e+Active+%28com+CTA%29.png?expires=1786536000&signature=989507c836235263456d1643ecd2b2cfdc790819b8342dd2ba98f18acc1490fe&req=dSIjFc57lIZZXPMW3nq%2BgaDHRoK8%2FGcjmh7h%2BiPwVE5HnTLGSkBsGCe0FNWa%0A9MyVfOuLz%2B7FJTT%2FhfNePAufMQU%3D%0A)](https://universidade.ploomes.com/courses/check-in-e-check-out)

---

**Esse artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
