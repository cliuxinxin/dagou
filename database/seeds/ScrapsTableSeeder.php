<?php

use Illuminate\Database\Seeder;

class ScrapsTableSeeder extends Seeder
{
    /**
     * Run the database seeds.
     *
     * @return void
     */
    public function run()
    {
        DB::table('scraps')->insert([
            'name' => str_random(10),
            'url' => 'http://'.str_random(5).'.com',
        ]);
    }
}
