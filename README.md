<h1>Tugas Besar IF1201 Dasar Pemrograman 2023</h1>
<h2>K03 - Kelompok 12</h2>
<ul>
<li> 16522066 / Chessy Anggraini Putri H</li>
<li> 19622309 / Nasywaa Anggun Athiefah</li>
<li> 19622075 / Moh Fairuz Alauddin Yahya</li>
<li> 16522093 / Goldwin Sonick Wijaya Thaha</li>
</ul>

<h2>Skema Commit dan Penggunaan Git</h2>
<ul>
<li> Setiap fitur baru harus dibuat dalam branch baru dengan nama feature</li>
  contoh : jika ingin membuat fitur Jin, maka beri nama branch Jin</li>
<li> Setiap fitur yang sudah dibuat dilakukan PR (Pull Request) ke branch develop</li>
<li> Nantinya (Fairuz) bakal squash and merge ke main</li>
<li> Jangan lupa untuk selalu pull develop untuk mencegah conflict</li>
<li> Untuk semantic commits, message commit buat dalam format berikut </li>
<ul>
    <li> Secara garis besar formatnya adalah 'feat/fix(branch_name): message commit detail"
        feat: a new feature, or change to existing feature.
        fix: Fixing a bug or known issue in code.</li>
</ul>
</ul>

<h2>Secara Garis Besar</h2>  
<ul>
<li> Copy message ini https://github.com/goldwinsonick/tubes-daspro-2023.git</li>
<li> Clone pada terminal dengan mengetik : git clone https://github.com/goldwinsonick/tubes-daspro-2023.git</li>
<li> Buat develop pada file lokal anda dengan buat branch lokal baru : git checkout -b develop</li>
<li> Lalu pull dulu dengan mengetik : git pull origin develop</li>
<li> Untuk fitur baru anda harus buat branch baru dengan mengetik : git checkout -b nama_branch </li>
<li> Silahkan lakukan perubahan sesuka anda di branch tersebut</li>
<li> Untuk menambahkan file yang telah anda kerjakan lakukan skema berikut: </li>
<ul>
    <li> Untuk menambahkan semua file pada branch lokal anda tulis : git add . </li>
    <li> Lalu commit dengan tulis : git commit -m "feat(nama_branch): Message commit", message commit diisi dengan detail    perubahan yang dilakukan, misalnya feat(jin): Menambahkan fungsi jin pembangun untuk membangun candi</li>
    <li> Lalu push ke repo dengan menulis: git push origin nama_branch</li>

</ul>
</ul>