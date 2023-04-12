Tugas Besar IF1201 Dasar Pemrograman 2023

<h2>K03 - Kelompok 12</h2>
- 16522066 / Chessy Anggraini Putri H
- 19622309 / Nasywaa Anggun Athiefah
- 19622075 / Moh Fairuz Alauddin Yahya
- 16522093 / Goldwin Sonick Wijaya Thaha

<h2>Skema Commit dan Penggunaan Git</h2>
- Setiap fitur baru harus dibuat dalam branch baru dengan nama <feature>,
  contoh : jika ingin membuat fitur Jin, maka beri nama branch Jin
- Setiap fitur yang sudah dibuat dilakukan PR (Pull Request) ke branch develop
- Nantinya (Fairuz) bakal squash and merge ke main
- Jangan lupa untuk selalu pull develop untuk mencegah conflict
- Untuk semantic commits, message commit buat dalam format berikut 
    -- Secara garis besar formatnya adalah 'feat/fix(branch_name): message commit detail"
        feat: a new feature, or change to existing feature.
        fix: Fixing a bug or known issue in code.

<h2>Secara Garis Besar</h2>  
- Copy message ini https://github.com/goldwinsonick/tubes-daspro-2023.git
- Clone pada terminal dengan mengetik : git clone https://github.com/goldwinsonick/tubes-daspro-2023.git
- Buat develop pada file lokal anda dengan buat branch lokal baru : git checkout -b develop
- Lalu pull dulu dengan mengetik : git pull origin develop
- Untuk fitur baru anda harus buat branch baru dengan mengetik : git checkout -b <nama_branch>
- Silahkan lakukan perubahan sesuka anda di branch tersebut
- Untuk menambahkan file yang telah anda kerjakan lakukan skema berikut: 
    -- Untuk menambahkan semua file pada branch lokal anda tulis : git add .
    -- Lalu commit dengan tulis : git commit -m "feat(nama_branch): Message commit", message commit diisi dengan detail    perubahan yang dilakukan, misalnya feat(jin): Menambahkan fungsi jin pembangun untuk membangun candi
    -- Lalu push ke repo dengan menulis: git push origin nama_branch



