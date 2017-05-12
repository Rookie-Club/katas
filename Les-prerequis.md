- Un ordinateur portable.
- Un terminal unix (pour windows, installer [cygwin](https://www.cygwin.com/) par exemple).
- [Git](https://git-scm.com/) installé.
- Un compte [github](https://github.com), en attendant autre chose.
- Une clef [SSH](http://fr.wikipedia.org/wiki/OpenSSH) publique.
- [Tmux](https://tmux.github.io/) installé dessus.
- S'assurer que [Vi(m)](http://www.vim.org/) est installé sur la machine (ou Emacs).
- Configurer le ssh pour accueillir une session tmux.
- [Optionnel] Installer [Docker](https://www.docker.com/).

Les trucs pour partager une session tmux

<pre>
command="/usr/bin/tmux -L rookieclub attach",no-port-forwarding,no-X11-forwarding,no-agent-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDa8kidBDEzDlGuRWCQ6BKV5/8qhayXqqrVaaXnt4sxM7R3+C6qSsfUpzktGrpGdUDdKKOmLGLgwcekhSsguNva1PHUAEyY07R1Qbbb8JAkxjL2mJfJh1apJz6oL/0i8Wb933Fdxe5s0lceh+VDZnGX7idaADLlsTlLdFnXlC/4s7WE2pegkD5rtPfNGMvrSp6ofIHky2TddbYQWLoXU94QkSxRGYok6epl9VGJbGFWNg3NWSPbpOx8MnJv7WX7uOzfpkpT0p+Y63KnSQOv/ES0qwAzEubIwQs8EU44itzWkWeW1SRrJkPKY/tS4rVtNofVXTFZoBToKGqDU3AlIGMd sims38930@gmail.com
command="/usr/bin/tmux -L rookieclub attach",no-port-forwarding,no-X11-forwarding,no-agent-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDfQXcBQLRvNJ2V3V6gzrWO25iBHeX2M3+vj8LSRwpZgrzWjSEEgJPfswmzg9lAuv2uXuFS+Ju2eW6v77c359g4mnQVhWmQIazKMWU5jtgwXO5FNCzWiGYZ5A9lvRKkbVdjze8GS30vdX0xCyL9bBylbBU9W8+YzSJiV3Lomzb54xMNsl9okMJID5KEDD1aB6ejZtYUTb+5Op1lJfyDJe75HZJfmSv5XRaczqsZM6b37EgthRdTgTvbuhr5BInWCVleKRkzdJEBNJPasjYYV5Lrl1e8chuvvwBP0InBDxfRqufvoCuZ6fVzldxuSV5mBR8zmbQg2P4NuLDBVC65V3gp hafid.traikzi@gmail.com
command="/usr/bin/tmux -L rookieclub attach",no-port-forwarding,no-X11-forwarding,no-agent-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDDWA7UHaLHR+JjDBFz3UmxaoSc+BUQu98wIIbUXCmbNrniO+WAtdQcXPuSjy/jb7/X08az0pwGyoGOsFXemiiDrtCmc5SE/2ArUZDM0FxSUGXt6OxX2R5sod4Gt8wtuHrPp1oBysI3tjuvLucvIkYZUsfzH/rUNvLTlNvrhv0TeAHg0pijbGOnM9POS7HMJzzJYPKyWakKlhpfycZL/E2z3zpGA/gR2uOolQGV61d9/kEHJNkTaHgianTV+qkdmdmgu25eH54aK7Wa7pWwfrd/yQo3Afu9D6mrlPytcTe7Iss4WIlv+gHJnhog/mX3dl20l6MH0C/YuBdib27JjWPp yannick@ut7.fr
command="/usr/bin/tmux -L rookieclub attach",no-port-forwarding,no-X11-forwarding,no-agent-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDsBG/Icp9cJ4kd8FriCji5FsZB0UVol29SeqaRDDzKKM8Bw23h1N0D5FHzZY/RWOq8PBegntZf9bOSlCvdXE0wxjOkhce3iQKbTFSdghlbEe/uduumDTndWqCVCu7/AcnxhMK/tEp3bMp6F9yDE/Ied8qogQzi3hSws5cDwEgsj7fCV6U55fDv0UvVHWL7SFtd8bZ/2xP6EX4yArFSX50xdwjRQmx3UtYJa51J34P1Qp20G23Wo5qp979dhTJCQUviuTIbkAc7WfAnHTEMVZhazHfharEGs4toI/NAYCaSTS4kR8DOZEayK0nPV5zG7u4p5D1U7VtvxbBQFPEqOgsx bosco.yohann@gmail.com
command="/usr/bin/tmux -L rookieclub attach",no-port-forwarding,no-X11-forwarding,no-agent-forwarding ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC9psORb39Ht7NiphBBjRaJIVZDmdiHYMEGZWytRoLK1flhYqp6oYIxIRG9ZpcNxmL+c+7sVNW/RnR0xoJ2ZqGBrfmP4WKCYHktDL+mayv4fkti1F9ZODaR4IH0AQx2AckoAsHRZT/vfMbWdWnZK8q1N9zrU+WBaePHJOOPdksGRz0rkt4rz4b7Z2XRKGjYpuurPu4sPNn0O92XKhTxADcI+2utp3jaToiGB6lF3nCh4Ajz1o1Z17bIdLkrILzL592SEkaSr1EWC4WyW89JYpg0f/hybNgDAhwwOhYdQbCDzJDyHhUT1q9Mgb/WEGCMGXxh2tTmIQy/Jfw/MZ1cScin carole.gombauld@gmail.com
</pre>

