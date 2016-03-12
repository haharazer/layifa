<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class Discounts extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::create('discounts', function(Blueprint $table) {
            $table->increments('id');
            $table->string('url', 1023);
            $table->string('title', 1023);
            $table->string('content', 1023);
            $table->string('price', 1023);
            $table->string('mall', 1023);
            $table->unsignedBigInteger('timestamp');
            $table->string('ori_url', 1023);
            $table->string('ori_pic_url', 1023);
            $table->string('category', 20);
            $table->string('pic_url', 1023);
            $table->string('source', 20);
            $table->integer('article_id');
            $table->string('tags', 1000);
            $table->integer('tag_id');
            $table->string('tag', 10);

            $table->timestamp('created_at')->default(DB::raw('CURRENT_TIMESTAMP'));
            $table->timestamp('updated_at')->default(DB::raw('CURRENT_TIMESTAMP'));

            $table->unique('article_id');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        //
    }
}
