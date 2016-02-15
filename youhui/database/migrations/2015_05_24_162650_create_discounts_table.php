<?php

use Illuminate\Database\Schema\Blueprint;
use Illuminate\Database\Migrations\Migration;

class CreateDiscountsTable extends Migration
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
            $table->string('link', 1023);
            $table->string('img', 1023);
            $table->integer('articleid');

            $table->timestamp('created_at')->default(DB::raw('CURRENT_TIMESTAMP'));
            $table->timestamp('updated_at')->default(DB::raw('CURRENT_TIMESTAMP'));

            $table->unique('articleid');
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::drop('discounts');
    }
}
