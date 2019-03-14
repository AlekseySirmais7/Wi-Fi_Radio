
import os
import os
import shutil

def copy_rename(old_file_name, new_file_name):
        src_dir= os.curdir
        dst_dir= os.path.join(os.curdir+'/static')
        src_file = os.path.join(src_dir+'/newSongs' , old_file_name)
        shutil.copy(src_file,dst_dir)
        
        dst_file = os.path.join(dst_dir, old_file_name)
        new_dst_file_name = os.path.join(dst_dir, new_file_name)
        os.rename(dst_file, new_dst_file_name)



path_new_song_dir =  './newSongs'
new_files = os.listdir(path_new_song_dir)

new_file_c = []

for i in range(len(new_files)):
	if '.mp3' in new_files[i]: # only for mp3 files
		new_file_c.append(new_files[i])



add_files= set(new_file_c)


print('ADDED_FILES: ')
for ad_f in add_files:
	print(ad_f+'  ')

path_old_songs_dir = './static'
old_files = os.listdir(path_old_songs_dir)

already_files = set(old_files)

print('\n\nALREADY_FILES: ')


for al_f in already_files:
	print(al_f+'  ')


must_add = (add_files - already_files)
print('\n\nMUST ADD:')

for m_add in must_add:
	print(m_add+'  ')
	copy_rename(m_add , str(m_add).replace(' ','_'))
	os.remove('./newSongs/'+m_add) 

