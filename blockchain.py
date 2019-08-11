import time
import hashlib
import json
import string
import random


class Block():

    def __init__(self, msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, previous_hash):
        self.msg1 = msg1
        self.msg2 = msg2
        self.msg3 = msg3
        self.msg4 = msg4
        self.msg5 = msg5
        self.msg6 = msg6
        self.msg7 = msg7
        self.msg8 = msg8
        self.merkle_tree = []
        self.previous_hash = previous_hash
        self.time_stamp = time.asctime(time.localtime(time.time()))
        self.time_for_cal=time.localtime(time.time())
        self.nonce = 1
        self.hash = self.get_hash()

    def get_hash(self):
        self.merkle_tree.append("")
        hash256_1 = hashlib.sha256()
        hash256_2 = hashlib.sha256()
        hash256_3 = hashlib.sha256()
        hash256_4 = hashlib.sha256()
        hash256_5 = hashlib.sha256()
        hash256_6 = hashlib.sha256()
        hash256_7 = hashlib.sha256()
        hash256_8 = hashlib.sha256()
        hash256_9 = hashlib.sha256()
        hash256_10 = hashlib.sha256()
        hash256_11 = hashlib.sha256()
        hash256_12 = hashlib.sha256()
        hash256_13 = hashlib.sha256()
        hash256_14 = hashlib.sha256()
        hash256_15 = hashlib.sha256()
        hash256_16 = hashlib.sha256()
        hash256_1.update(self.msg1.encode('gb2312'))
        hash256_2.update(self.msg2.encode('gb2312'))
        hash256_3.update(self.msg3.encode('gb2312'))
        hash256_4.update(self.msg4.encode('gb2312'))
        hash256_5.update(self.msg5.encode('gb2312'))
        hash256_6.update(self.msg6.encode('gb2312'))
        hash256_7.update(self.msg7.encode('gb2312'))
        hash256_8.update(self.msg8.encode('gb2312'))
        hash256_9.update((hash256_1.hexdigest()+ hash256_2.hexdigest()).encode('gb2312'))
        hash256_10.update((hash256_3.hexdigest()+ hash256_4.hexdigest()).encode('gb2312'))
        hash256_11.update((hash256_5.hexdigest()+ hash256_6.hexdigest()).encode('gb2312'))
        hash256_12.update((hash256_7.hexdigest()+ hash256_8.hexdigest()).encode('gb2312'))
        hash256_13.update((hash256_9.hexdigest()+ hash256_10.hexdigest()).encode('gb2312'))
        hash256_14.update((hash256_11.hexdigest()+ hash256_12.hexdigest()).encode('gb2312'))
        hash256_15.update((hash256_13.hexdigest()+ hash256_14.hexdigest()).encode('gb2312'))
        self.merkle_tree.append(hash256_15.hexdigest())
        self.merkle_tree.append(hash256_13.hexdigest())
        self.merkle_tree.append(hash256_14.hexdigest())
        self.merkle_tree.append(hash256_9.hexdigest())
        self.merkle_tree.append(hash256_10.hexdigest())
        self.merkle_tree.append(hash256_11.hexdigest())
        self.merkle_tree.append(hash256_12.hexdigest())
        self.merkle_tree.append(hash256_1.hexdigest())
        self.merkle_tree.append(hash256_2.hexdigest())
        self.merkle_tree.append(hash256_3.hexdigest())
        self.merkle_tree.append(hash256_4.hexdigest())
        self.merkle_tree.append(hash256_5.hexdigest())
        self.merkle_tree.append(hash256_6.hexdigest())
        self.merkle_tree.append(hash256_7.hexdigest())
        self.merkle_tree.append(hash256_8.hexdigest())
        data = self.time_stamp + self.merkle_tree[1] + str(self.nonce) + self.previous_hash
        hash256_16.update(data.encode('gb2312'))
        return hash256_16.hexdigest()

    def mine(self, diffculty):
        target = ''

        for each_num in range(0,diffculty):
            target = target + '0'
        while (int(self.hash[0:diffculty] != target)):
            self.nonce = self.nonce + 1
            self.hash = self.get_hash()
        print('Mined a new block')


class EduChain():

    def __init__(self, difficulty):
        self.list = []
        self.difficulty = difficulty
        self.message = []
    def block_dict(self, Block):
        return Block.__dict__
    def mine_time(self,Block):
        return Block.time_for_cal.tm_min*60+Block.time_for_cal.tm_sec
    def add_block(self, Block):
        Block.mine(self.difficulty)
        self.list.append(Block)

    def show(self,block_number):
        #json_res = json.dumps(self.list, default=self.block_dict, sort_keys = True, indent = 4, separators=(',', ': '))
        #print(json_res)
        print("Block ", block_number, ":")
        print("{")
        print(" message 1: ", self.list[block_number].msg1)
        print(" message 2: ", self.list[block_number].msg2)
        print(" message 3: ", self.list[block_number].msg3)
        print(" message 4: ", self.list[block_number].msg4)
        print(" message 5: ", self.list[block_number].msg5)
        print(" message 6: ", self.list[block_number].msg6)
        print(" message 7: ", self.list[block_number].msg7)
        print(" message 8: ", self.list[block_number].msg8)
        print(" merkle tree root: ", self.list[block_number].merkle_tree[1])
        print(" previous hash: ", self.list[block_number].previous_hash)
        print(" time stamp: ", self.list[block_number].time_stamp)
        print(" nonce: ", self.list[block_number].nonce)
        print(" block hash: ", self.list[block_number].hash)
        print("}")

    def isChainValid(self):
        for i in range(1, len(self.list)):
            current_block = self.list[i]
            previous_block = self.list[i - 1]
            if (current_block.hash != current_block.get_hash()):
                print('Current hash is not equal')
                return False
            if (current_block.previous_hash != previous_block.hash):
                print('Previous hash is not equal')
                return False
            print('All the blocks are correct')
            return True
    def check_message(self,number):
        number=number-1
        block_number=number//8+1
        message_number=number % 8 + 8
        locate_block=self.list[block_number]
        hash256_a = hashlib.sha256()
        hash256_b = hashlib.sha256()
        hash256_c = hashlib.sha256()
        hash256_d = hashlib.sha256()
        hash256_a.update(self.message[number].encode('gb2312'))
        message_hash=hash256_a.hexdigest()
        for i in range(1,4):
            if(i==1):
                if(message_number%2==0):
                    hash256_b.update((message_hash+locate_block.merkle_tree[message_number+1]).encode('gb2312'))
                else:
                    hash256_b.update(( locate_block.merkle_tree[message_number - 1] + message_hash ).encode('gb2312'))
                tmp = hash256_b.hexdigest()
                message_number=message_number//2
            elif(i==2):
                if (message_number % 2 == 0):
                    hash256_c.update((tmp + locate_block.merkle_tree[message_number + 1]).encode('gb2312'))
                else:
                    hash256_c.update((locate_block.merkle_tree[message_number - 1] + tmp).encode('gb2312'))
                tmp = hash256_c.hexdigest()
                message_number = message_number // 2
            elif (i == 3):
                if (message_number % 2 == 0):
                    hash256_d.update((tmp + locate_block.merkle_tree[message_number + 1]).encode('gb2312'))
                else:
                    hash256_d.update((locate_block.merkle_tree[message_number - 1] + tmp).encode('gb2312'))
                tmp = hash256_d.hexdigest()
                message_number = message_number // 2

        if(tmp!=locate_block.merkle_tree[1]):
            print(self.message[number] , " this message is not the correct message")
        else:
            print(self.message[number] , " this message is correct, and it is located in Block ",block_number)

    def message_generator(self):
        chars = string.ascii_uppercase + string.digits
        word = ''.join(random.choice(chars) for _ in range(6))
        self.message.append(word)

   # def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    #    return ''.join(random.choice(chars) for _ in range(size))



print('EduChain CLT Apr 2018 by fxt0706')
c = EduChain(4)
c.add_block(Block("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", '0'))
message_length=0
check_block_length=0
check_message_length=0
#line_pointer=0
j=0
while(1):
    with open('message.txt', mode='r') as file:
       lines = file.readlines()
       file.seek(0)
       if(message_length!=len(lines)):
            if (len(lines) % 8 == 0):

                #file.seek(,message_length)
                for line in file.readlines()[message_length:len(lines)]:
                    # print(line)
                    line = line.strip('\n')
                    c.message.append(str(line))
                 # 讀取交易訊息
                c.add_block(Block(c.message[8 * j], c.message[8 * j + 1], c.message[8 * j + 2], c.message[8 * j + 3],
                              c.message[8 * j + 4], c.message[8 * j + 5], c.message[8 * j + 6], c.message[8 * j + 7],
                              c.list[len(c.list) - 1].hash))
                j=j+1
                #line_pointer=lines
                message_length=len(lines)
    #print(lines)

    #print(c.message[2])
    #for j in range(0, len(c.message) // 8):

    with open('check_block.txt', mode='r') as file1:
        lines = file1.readlines()
        file1.seek(0)
        if (check_block_length != len(lines)):
            file1.seek(check_block_length)
            for line in file1:
                #line = line.strip()
                line = line.strip('\n')
                if(line.strip()):
                    c.show(int(line))
            check_block_length=len(lines)
    with open('check_message.txt', mode='r') as file2:
        lines = file2.readlines()
        file2.seek(0)
        if (check_message_length != len(lines)):
            file2.seek(check_message_length)
            for line in file2:
                # line = line.strip()
                line = line.strip('\n')
                if (line.strip()):
                    c.check_message(int(line))
            check_message_length = len(lines)
     #   for line in file:
      #      c.check_message(int(line))
#for i i range(1,33):
    #c.message_generator()


#c.show(3)
#c.isChainValid()
#c.check_message(20)
#json_res = json.dumps(tmine, sort_keys=True, indent=4, separators=(',', ': '))
#print(json_res)